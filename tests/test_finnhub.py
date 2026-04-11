from unittest.mock import patch, MagicMock
import pytest
from db import get_db, init_db
from collector.finnhub import collect_finnhub


@pytest.fixture(autouse=True)
def set_finnhub_key(monkeypatch):
    monkeypatch.setenv("FINNHUB_API_KEY", "test-key")


@pytest.fixture
def db():
    conn = get_db(":memory:")
    init_db(conn)
    yield conn
    conn.close()


FAKE_CALENDAR = {
    "economicCalendar": [
        {"country": "US", "event": "FOMC Rate Decision", "impact": "high",
         "time": "2026-04-15 14:00:00", "actual": "3.25", "estimate": "3.25",
         "prev": "3.50", "unit": "%"},
        {"country": "KR", "event": "BOK Interest Rate", "impact": "high",
         "time": "2026-04-16 09:00:00", "actual": "2.75", "estimate": "2.75",
         "prev": "3.00", "unit": "%"},
        {"country": "JP", "event": "BOJ Rate", "impact": "high",
         "time": "2026-04-17 00:00:00", "actual": "0.5", "estimate": "0.5",
         "prev": "0.25", "unit": "%"},  # Not US/KR
        {"country": "US", "event": "Housing Starts", "impact": "low",
         "time": "2026-04-15 08:30:00", "actual": "1.4M", "estimate": "1.3M",
         "prev": "1.3M", "unit": ""},  # low impact
    ]
}


@patch("collector.finnhub.requests.get")
def test_collect_finnhub_filters_country_impact(mock_get, db):
    resp = MagicMock()
    resp.raise_for_status = MagicMock()
    resp.json.return_value = FAKE_CALENDAR
    mock_get.return_value = resp

    count = collect_finnhub(db)
    # Only US+KR with high/medium impact: FOMC (US, high) + BOK (KR, high) = 2
    assert count == 2


@patch("collector.finnhub.requests.get")
def test_collect_finnhub_no_duplicates(mock_get, db):
    resp = MagicMock()
    resp.raise_for_status = MagicMock()
    resp.json.return_value = FAKE_CALENDAR
    mock_get.return_value = resp

    collect_finnhub(db)
    count = collect_finnhub(db)
    assert count == 0


@patch("collector.finnhub.requests.get")
def test_collect_finnhub_sets_domain_macro(mock_get, db):
    resp = MagicMock()
    resp.raise_for_status = MagicMock()
    resp.json.return_value = FAKE_CALENDAR
    mock_get.return_value = resp

    collect_finnhub(db)
    cursor = db.execute("SELECT domain FROM sources WHERE source_type='finnhub' LIMIT 1")
    assert cursor.fetchone()[0] == "macro"
