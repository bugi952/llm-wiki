import logging
import os
import sqlite3

import yaml
from fredapi import Fred

logger = logging.getLogger(__name__)


def _load_series():
    """Load FRED series config from macro.yaml."""
    with open("config/sources/macro.yaml") as f:
        cfg = yaml.safe_load(f)
    return cfg.get("fred", {}).get("series", [])


def collect_fred(conn):
    """Collect latest values from FRED API.

    Returns number of new entries inserted.
    """
    api_key = os.environ.get("FRED_API_KEY", "")
    if not api_key:
        logger.warning("FRED_API_KEY not set, skipping FRED collection")
        return 0

    fred = Fred(api_key=api_key)
    series_list = _load_series()
    total_new = 0

    for series_cfg in series_list:
        series_id = series_cfg["id"]
        series_name = series_cfg["name"]

        try:
            data = fred.get_series(series_id, observation_start="2026-01-01")
            if data is None or data.empty:
                continue

            latest_date = data.index[-1].strftime("%Y-%m-%d")
            latest_value = float(data.iloc[-1])

            # Check if we already have this date for this series
            cursor = conn.execute(
                "SELECT id FROM sources WHERE source_type='fred' AND feed_name=? AND published_at=?",
                (series_id, latest_date),
            )
            if cursor.fetchone():
                continue

            title = f"{series_name}: {latest_value:.1f} ({latest_date})"
            content = f"시리즈: {series_id}\n이름: {series_name}\n날짜: {latest_date}\n값: {latest_value}"
            url = f"https://fred.stlouisfed.org/series/{series_id}"

            conn.execute(
                """INSERT INTO sources
                   (source_type, feed_name, domain, title, url, content, published_at, status)
                   VALUES ('fred', ?, 'macro', ?, ?, ?, ?, 'collected')""",
                (series_id, title, url, content, latest_date),
            )
            total_new += 1
            logger.info("FRED %s: %s = %.1f", series_id, latest_date, latest_value)

        except sqlite3.IntegrityError:
            pass
        except Exception as e:
            logger.warning("FRED %s failed: %s", series_id, e)

    conn.commit()
    return total_new
