import logging
import os
import sqlite3
from datetime import date, timedelta

import requests
import yaml

logger = logging.getLogger(__name__)

FINNHUB_API_URL = "https://finnhub.io/api/v1/calendar/economic"


def _load_config():
    """Load Finnhub config from macro.yaml."""
    with open("config/sources/macro.yaml") as f:
        cfg = yaml.safe_load(f)
    return cfg.get("finnhub", {})


def collect_finnhub(conn):
    """Collect economic calendar events from Finnhub.

    Returns number of new entries inserted.
    """
    api_key = os.environ.get("FINNHUB_API_KEY", "")
    if not api_key:
        logger.warning("FINNHUB_API_KEY not set, skipping Finnhub collection")
        return 0

    cfg = _load_config()
    countries = set(cfg.get("countries", ["US", "KR"]))
    min_impact = cfg.get("min_impact", "medium")
    impact_levels = {"high"} if min_impact == "high" else {"high", "medium"}

    today = date.today()
    from_date = today.isoformat()
    to_date = (today + timedelta(days=7)).isoformat()

    try:
        resp = requests.get(
            FINNHUB_API_URL,
            params={"from": from_date, "to": to_date, "token": api_key},
            timeout=15,
        )
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logger.warning("Finnhub API error (may require premium): %s", e)
        return 0
    data = resp.json()

    events = data.get("economicCalendar", [])
    total_new = 0

    for event in events:
        country = event.get("country", "")
        impact = event.get("impact", "").lower()
        event_name = event.get("event", "")
        event_time = event.get("time", "")

        if country not in countries:
            continue
        if impact not in impact_levels:
            continue

        actual = event.get("actual", "")
        estimate = event.get("estimate", "")
        prev = event.get("prev", "")
        unit = event.get("unit", "")

        title = f"[{country}] {event_name}"
        if actual:
            title += f": {actual}{unit}"

        date_str = event_time[:10] if event_time else today.isoformat()
        content = (
            f"이벤트: {event_name}\n국가: {country}\n영향: {impact}\n"
            f"시간: {event_time}\n실제: {actual}\n예상: {estimate}\n이전: {prev}"
        )
        url = f"https://finnhub.io/calendar/economic?country={country}&date={date_str}"

        try:
            conn.execute(
                """INSERT INTO sources
                   (source_type, feed_name, domain, title, url, content, published_at, status)
                   VALUES ('finnhub', ?, 'macro', ?, ?, ?, ?, 'collected')""",
                (event_name, title, url, content, date_str),
            )
            total_new += 1
        except sqlite3.IntegrityError:
            pass

    conn.commit()
    logger.info("Finnhub: %d events (from %d total, countries=%s)", total_new, len(events), countries)
    return total_new
