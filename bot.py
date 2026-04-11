import logging
import os
from datetime import date, timedelta

from dotenv import load_dotenv

load_dotenv()

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from db import get_db, init_db, get_daily_api_count
from collector.manual import process_input, run_pipeline_for_source
from scheduler import acquire_lock, release_lock

logger = logging.getLogger(__name__)

CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")


def _get_status_counts(conn):
    """Get counts by status."""
    counts = {}
    for status in ["collected", "topic_pass", "topic_fail", "quality_pass", "quality_fail", "ingested"]:
        cursor = conn.execute("SELECT COUNT(*) FROM sources WHERE status = ?", (status,))
        counts[status] = cursor.fetchone()[0]
    counts["api_today"] = get_daily_api_count(conn)
    return counts


def _get_recent_items(conn, limit=5):
    """Get most recently ingested items."""
    cursor = conn.execute(
        "SELECT title, url, importance FROM sources WHERE status='ingested' ORDER BY id DESC LIMIT ?",
        (limit,),
    )
    return [{"title": r[0], "url": r[1], "importance": r[2]} for r in cursor.fetchall()]


def _get_weekly_stats(conn):
    """Get stats for the past 7 days."""
    week_ago = (date.today() - timedelta(days=7)).isoformat()
    cursor = conn.execute(
        """SELECT SUM(total_collected), SUM(topic_passed), SUM(quality_passed), SUM(ingested)
           FROM filter_stats WHERE date >= ?""",
        (week_ago,),
    )
    row = cursor.fetchone()
    if not row or row[0] is None:
        return {"collected": 0, "topic_passed": 0, "quality_passed": 0, "ingested": 0}
    return {
        "collected": row[0] or 0,
        "topic_passed": row[1] or 0,
        "quality_passed": row[2] or 0,
        "ingested": row[3] or 0,
    }


async def cmd_add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /add command — immediate pipeline for manual input."""
    text = " ".join(context.args) if context.args else ""
    if not text:
        await update.message.reply_text("사용법: /add [URL 또는 텍스트]")
        return

    conn = get_db()
    init_db(conn)

    source_id = process_input(conn, text)
    if source_id is None:
        await update.message.reply_text("이미 등록된 소스입니다.")
        conn.close()
        return

    await update.message.reply_text("처리 중...")

    if not acquire_lock():
        await update.message.reply_text("파이프라인 실행 중. 잠시 후 다시 시도해주세요.")
        conn.close()
        return

    try:
        run_pipeline_for_source(conn, source_id)

        # Check result
        cursor = conn.execute("SELECT status, importance, vault_path FROM sources WHERE id=?", (source_id,))
        row = cursor.fetchone()
        if row and row[0] == "ingested":
            msg = f"Wiki 추가 완료: {text[:100]}\n중요도: {row[1]}"
        elif row and row[0] == "quality_fail":
            msg = f"품질 기준 미달로 스킵됨: {text[:100]}"
        else:
            msg = f"처리 완료 (상태: {row[0] if row else 'unknown'})"

        await update.message.reply_text(msg)
    finally:
        release_lock()
        conn.close()


async def cmd_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /status command."""
    conn = get_db()
    init_db(conn)
    counts = _get_status_counts(conn)
    conn.close()

    msg = (
        f"📊 현황\n"
        f"수집 대기: {counts['collected']}\n"
        f"토픽 통과: {counts['topic_pass']}\n"
        f"품질 통과: {counts['quality_pass']}\n"
        f"Wiki 저장: {counts['ingested']}\n"
        f"CLI 호출: {counts['api_today']}/300"
    )
    await update.message.reply_text(msg)


async def cmd_recent(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /recent command."""
    conn = get_db()
    init_db(conn)
    items = _get_recent_items(conn)
    conn.close()

    if not items:
        await update.message.reply_text("최근 추가된 항목 없음")
        return

    lines = ["📋 최근 Wiki 추가:"]
    for item in items:
        tag = f"[{item['importance']}]" if item["importance"] else ""
        lines.append(f"• {tag} {item['title']}")

    await update.message.reply_text("\n".join(lines))


async def cmd_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /stats command."""
    conn = get_db()
    init_db(conn)
    stats = _get_weekly_stats(conn)
    conn.close()

    msg = (
        f"📈 주간 통계 (최근 7일)\n"
        f"수집: {stats['collected']}건\n"
        f"필터 통과: {stats['quality_passed']}건\n"
        f"Wiki 추가: {stats['ingested']}건"
    )
    await update.message.reply_text(msg)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle plain text messages — treat as /add."""
    if not update.message or not update.message.text:
        return
    context.args = update.message.text.split()
    await cmd_add(update, context)


async def notify_urgent(app, title, summary):
    """Send urgent source notification."""
    if CHAT_ID:
        msg = f"🔴 긴급: {title}\n{summary}"
        await app.bot.send_message(chat_id=CHAT_ID, text=msg)


async def send_weekly_report(app):
    """Send weekly report via Telegram. Called from scheduler on Sundays."""
    if not CHAT_ID:
        return

    conn = get_db()
    init_db(conn)
    stats = _get_weekly_stats(conn)

    from wiki.linter import lint_vault, format_report
    lint_report = lint_vault()
    lint_text = format_report(lint_report)

    conn.close()

    msg = (
        f"📊 주간 리포트\n"
        f"수집: {stats['collected']}건\n"
        f"필터 통과: {stats['quality_passed']}건\n"
        f"Wiki 추가: {stats['ingested']}건\n\n"
        f"{lint_text}"
    )
    await app.bot.send_message(chat_id=CHAT_ID, text=msg)


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")

    token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN not set")
        return

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("add", cmd_add))
    app.add_handler(CommandHandler("status", cmd_status))
    app.add_handler(CommandHandler("recent", cmd_recent))
    app.add_handler(CommandHandler("stats", cmd_stats))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Bot started")
    app.run_polling()


if __name__ == "__main__":
    main()
