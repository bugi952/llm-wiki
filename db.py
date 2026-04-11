import sqlite3
from datetime import date


def get_db(path="data/wiki.db"):
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db(conn):
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS sources (
            id INTEGER PRIMARY KEY,
            source_type TEXT NOT NULL,
            feed_name TEXT,
            domain TEXT,
            title TEXT NOT NULL,
            url TEXT,
            story_url TEXT,
            content TEXT,
            published_at DATETIME,
            collected_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'collected',
            importance TEXT,
            filter_a_result TEXT,
            filter_b_result TEXT,
            vault_path TEXT,
            indexed BOOLEAN DEFAULT 0,
            UNIQUE(url),
            UNIQUE(story_url)
        );

        CREATE TABLE IF NOT EXISTS filter_stats (
            id INTEGER PRIMARY KEY,
            date DATE NOT NULL,
            total_collected INTEGER DEFAULT 0,
            topic_passed INTEGER DEFAULT 0,
            topic_failed INTEGER DEFAULT 0,
            quality_passed INTEGER DEFAULT 0,
            quality_failed INTEGER DEFAULT 0,
            ingested INTEGER DEFAULT 0,
            UNIQUE(date)
        );

        CREATE TABLE IF NOT EXISTS system_log (
            id INTEGER PRIMARY KEY,
            event TEXT NOT NULL,
            details TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()


def log_event(conn, event, details=None):
    conn.execute(
        "INSERT INTO system_log (event, details) VALUES (?, ?)",
        (event, details),
    )
    conn.commit()


def get_daily_api_count(conn):
    cursor = conn.execute(
        "SELECT COUNT(*) FROM system_log WHERE event = 'api_call' AND date(created_at) = ?",
        (date.today().isoformat(),),
    )
    return cursor.fetchone()[0]


def increment_api_count(conn):
    log_event(conn, "api_call")
