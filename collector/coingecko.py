"""Collect crypto prices from CoinGecko free API (no key needed)."""

import logging
import sqlite3
from datetime import date

import requests

logger = logging.getLogger(__name__)

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"
COINS = {
    "bitcoin": "BTC",
    "ethereum": "ETH",
    "hyperliquid": "HYPE",
}


def collect_coingecko(conn):
    """Collect latest crypto prices. Returns number of new entries."""
    try:
        resp = requests.get(
            COINGECKO_URL,
            params={
                "ids": ",".join(COINS.keys()),
                "vs_currencies": "usd",
                "include_24hr_change": "true",
            },
            timeout=15,
        )
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.warning("CoinGecko API error: %s", e)
        return 0

    data = resp.json()
    today = date.today().isoformat()
    total_new = 0

    for coin_id, symbol in COINS.items():
        if coin_id not in data:
            continue

        price = data[coin_id].get("usd", 0)
        change_24h = data[coin_id].get("usd_24h_change", 0)
        change_str = f"{change_24h:+.1f}%" if change_24h else ""

        title = f"{symbol}: ${price:,.2f} ({change_str})"
        content = f"코인: {symbol}\n가격: ${price:,.2f}\n24h 변동: {change_str}\n날짜: {today}"
        url = f"https://www.coingecko.com/en/coins/{coin_id}"

        try:
            conn.execute(
                """INSERT INTO sources
                   (source_type, feed_name, domain, title, url, content, published_at, status)
                   VALUES ('coingecko', ?, 'crypto', ?, ?, ?, ?, 'collected')""",
                (symbol, title, url, content, today),
            )
            total_new += 1
        except sqlite3.IntegrityError:
            pass

    conn.commit()
    logger.info("CoinGecko: %d prices collected", total_new)
    return total_new
