import logging
import os
import sqlite3

import requests
import yaml

logger = logging.getLogger(__name__)

ECOS_API_URL = "https://ecos.bok.or.kr/api/StatisticSearch"


def _load_series():
    """Load ECOS series config from macro.yaml."""
    with open("config/sources/macro.yaml") as f:
        cfg = yaml.safe_load(f)
    return cfg.get("ecos", {}).get("series", [])


def collect_ecos(conn):
    """Collect latest values from Bank of Korea ECOS API.

    Returns number of new entries inserted.
    """
    api_key = os.environ.get("ECOS_API_KEY", "")
    if not api_key:
        logger.warning("ECOS_API_KEY not set, skipping ECOS collection")
        return 0

    series_list = _load_series()
    total_new = 0

    for series_cfg in series_list:
        stat_code = series_cfg["code"]
        series_name = series_cfg["name"]

        try:
            url = f"{ECOS_API_URL}/{api_key}/json/kr/1/1/{stat_code}/M/202601/202612"
            resp = requests.get(url, timeout=15)
            resp.raise_for_status()
            data = resp.json()

            rows = data.get("StatisticSearch", {}).get("row", [])
            if not rows:
                continue

            latest = rows[-1]
            time_str = latest.get("TIME", "")
            value = latest.get("DATA_VALUE", "")

            # Format date: 202603 -> 2026-03
            date_str = f"{time_str[:4]}-{time_str[4:6]}" if len(time_str) >= 6 else time_str

            # Check duplicate
            cursor = conn.execute(
                "SELECT id FROM sources WHERE source_type='ecos' AND feed_name=? AND published_at=?",
                (stat_code, date_str),
            )
            if cursor.fetchone():
                continue

            title = f"{series_name}: {value} ({date_str})"
            content = f"통계코드: {stat_code}\n이름: {series_name}\n기간: {date_str}\n값: {value}"
            source_url = f"https://ecos.bok.or.kr/api/StatisticSearch/{stat_code}"

            conn.execute(
                """INSERT INTO sources
                   (source_type, feed_name, domain, title, url, content, published_at, status)
                   VALUES ('ecos', ?, 'macro', ?, ?, ?, ?, 'collected')""",
                (stat_code, title, source_url, content, date_str),
            )
            total_new += 1
            logger.info("ECOS %s: %s = %s", stat_code, date_str, value)

        except sqlite3.IntegrityError:
            pass
        except Exception as e:
            logger.warning("ECOS %s failed: %s", stat_code, e)

    conn.commit()
    return total_new
