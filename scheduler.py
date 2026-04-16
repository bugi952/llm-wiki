import json
import logging
import os
import sys
import time

import yaml
from dotenv import load_dotenv

load_dotenv()

from db import get_db, init_db, log_event, get_daily_api_count
from collector.rss import collect_rss
from collector.hackernews import collect_hackernews
from collector.fred import collect_fred
from collector.ecos import collect_ecos
from collector.finnhub import collect_finnhub
from collector.coingecko import collect_coingecko
from filter.topic import filter_topic
from filter.quality import filter_quality
from wiki.ingest import ingest
from wiki.indexer import update_index
from sync import sync_vault

logger = logging.getLogger(__name__)

LOCK_FILE = "data/pipeline.lock"
API_DAILY_LIMIT = 300
STALE_LOCK_SECONDS = 3600  # 1 hour


def acquire_lock():
    """Try to acquire pipeline lock. Returns True if acquired."""
    if os.path.exists(LOCK_FILE):
        mtime = os.path.getmtime(LOCK_FILE)
        age = time.time() - mtime
        if age > STALE_LOCK_SECONDS:
            logger.warning("Stale lock removed (age: %ds)", int(age))
            os.remove(LOCK_FILE)
        else:
            logger.warning("Pipeline already running (lock age: %ds)", int(age))
            return False

    os.makedirs(os.path.dirname(LOCK_FILE), exist_ok=True)
    with open(LOCK_FILE, "w") as f:
        f.write(str(os.getpid()))
    return True


def release_lock():
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)


def _load_feeds():
    """Load RSS feed configs from YAML files."""
    feeds = []
    for path in ["config/sources/ai.yaml", "config/sources/macro.yaml", "config/sources/crypto.yaml"]:
        if not os.path.exists(path):
            continue
        with open(path) as f:
            cfg = yaml.safe_load(f)
        for feed in cfg.get("rss_feeds", []):
            feeds.append(feed)
    return feeds


def run_auto(conn):
    """Run full pipeline: collect → filter → ingest → index → sync.

    Returns dict with step counts.
    """
    result = {}

    # Lock
    if not acquire_lock():
        return {"error": "locked"}

    try:
        # API limit check
        if get_daily_api_count(conn) >= API_DAILY_LIMIT:
            logger.error("Daily API limit exceeded (%d)", API_DAILY_LIMIT)
            result["error"] = "api_limit_exceeded"
            return result

        # 1. Collect — all sources
        feeds = _load_feeds()
        rss_count = collect_rss(conn, feeds, delay=3)
        hn_count = collect_hackernews(conn)
        fred_count = collect_fred(conn)
        ecos_count = collect_ecos(conn)
        finnhub_count = collect_finnhub(conn)
        coingecko_count = collect_coingecko(conn)
        collected = rss_count + hn_count + fred_count + ecos_count + finnhub_count + coingecko_count
        result["collected"] = collected
        result["collected_detail"] = {
            "rss": rss_count, "hackernews": hn_count, "fred": fred_count,
            "ecos": ecos_count, "finnhub": finnhub_count, "coingecko": coingecko_count,
        }
        log_event(conn, "collect", json.dumps(result["collected_detail"]))

        # 2. Filter A: topic
        topic_passed, topic_failed = filter_topic(conn)
        result["topic_passed"] = topic_passed
        result["topic_failed"] = topic_failed

        # 3. Filter B: quality
        try:
            quality_passed, quality_failed = filter_quality(conn)
            result["quality_passed"] = quality_passed
            result["quality_failed"] = quality_failed
        except Exception as e:
            logger.error("Filter quality crashed, continuing to ingest: %s", e)
            result["quality_error"] = str(e)

        # 4. Ingest
        ingested = ingest(conn)
        result["ingested"] = ingested

        # 5. Index
        update_index(conn)

        # 6. Sync
        sync_result = sync_vault()
        result["sync"] = sync_result

        # 7. Update filter_stats
        _update_filter_stats(conn, result)

        log_event(conn, "pipeline", json.dumps(result))
        logger.info("Pipeline complete: %s", result)

    finally:
        release_lock()

    return result


def _update_filter_stats(conn, result):
    """Insert or update today's filter_stats row (UTC date)."""
    from datetime import datetime, timezone
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    try:
        conn.execute(
            """INSERT INTO filter_stats (date, total_collected, topic_passed, topic_failed,
               quality_passed, quality_failed, ingested)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (today, result.get("collected", 0), result.get("topic_passed", 0),
             result.get("topic_failed", 0), result.get("quality_passed", 0),
             result.get("quality_failed", 0), result.get("ingested", 0)),
        )
    except Exception:
        # Date already exists — accumulate
        conn.execute(
            """UPDATE filter_stats SET
               total_collected = total_collected + ?,
               topic_passed = topic_passed + ?,
               topic_failed = topic_failed + ?,
               quality_passed = quality_passed + ?,
               quality_failed = quality_failed + ?,
               ingested = ingested + ?
               WHERE date = ?""",
            (result.get("collected", 0), result.get("topic_passed", 0),
             result.get("topic_failed", 0), result.get("quality_passed", 0),
             result.get("quality_failed", 0), result.get("ingested", 0), today),
        )
    conn.commit()


def run_status(conn):
    """Print DB status summary."""
    for status in ["collected", "topic_pass", "topic_fail", "quality_pass", "quality_fail", "ingested"]:
        cursor = conn.execute("SELECT COUNT(*) FROM sources WHERE status = ?", (status,))
        count = cursor.fetchone()[0]
        print(f"  {status}: {count}")

    api_count = get_daily_api_count(conn)
    print(f"  API calls today: {api_count}/{API_DAILY_LIMIT}")


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")

    conn = get_db()
    init_db(conn)

    mode = sys.argv[1] if len(sys.argv) > 1 else "auto"

    if mode == "auto":
        run_auto(conn)
    elif mode == "collect":
        feeds = _load_feeds()
        rss = collect_rss(conn, feeds)
        hn = collect_hackernews(conn)
        fred = collect_fred(conn)
        ecos = collect_ecos(conn)
        finnhub = collect_finnhub(conn)
        print(f"Collected: RSS={rss} HN={hn} FRED={fred} ECOS={ecos} Finnhub={finnhub}")
    elif mode == "filter":
        tp, tf = filter_topic(conn)
        qp, qf = filter_quality(conn)
        print(f"Topic: {tp} passed, {tf} failed. Quality: {qp} passed, {qf} failed.")
    elif mode == "ingest":
        count = ingest(conn)
        update_index(conn)
        print(f"Ingested: {count}")
    elif mode == "sync":
        result = sync_vault()
        print(f"Sync: {result}")
    elif mode == "migrate":
        from wiki.migrate import migrate
        stats = migrate(conn)
        print(f"Migration complete: {stats}")
    elif mode == "status":
        run_status(conn)
    else:
        print(f"Unknown mode: {mode}")
        print("Usage: python scheduler.py [auto|collect|filter|ingest|sync|status|migrate]")
        sys.exit(1)

    conn.close()


if __name__ == "__main__":
    main()
