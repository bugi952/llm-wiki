"""Telegram notification utility for scheduler/pipeline alerts."""

import logging
import os

import requests

logger = logging.getLogger(__name__)

_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")


def send_alert(message):
    """Send a Telegram message. Fails silently on error."""
    if not _TOKEN or not _CHAT_ID:
        logger.warning("Telegram credentials not set, skipping alert")
        return
    try:
        requests.post(
            f"https://api.telegram.org/bot{_TOKEN}/sendMessage",
            json={"chat_id": _CHAT_ID, "text": message},
            timeout=10,
        )
    except Exception as e:
        logger.warning("Telegram alert failed: %s", e)
