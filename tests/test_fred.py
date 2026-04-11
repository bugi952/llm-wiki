import os
from unittest.mock import patch, MagicMock
import pytest
from db import get_db, init_db
from collector.fred import collect_fred


@pytest.fixture(autouse=True)
def set_fred_key(monkeypatch):
    monkeypatch.setenv("FRED_API_KEY", "test-key")


@pytest.fixture
def db():
    conn = get_db(":memory:")
    init_db(conn)
    yield conn
    conn.close()


FAKE_SERIES_DATA = {
    "GDP": {"date": "2026-01-01", "value": 28500.0, "name": "미국 GDP"},
    "CPIAUCSL": {"date": "2026-03-01", "value": 315.2, "name": "미국 CPI"},
}


def _mock_fred_get_series(series_id, **kwargs):
    import pandas as pd
    data = FAKE_SERIES_DATA.get(series_id)
    if not data:
        return pd.Series(dtype=float)
    return pd.Series([data["value"]], index=[pd.Timestamp(data["date"])])


@patch("collector.fred.Fred")
def test_collect_fred_inserts(mock_fred_cls, db):
    mock_fred = MagicMock()
    mock_fred.get_series.side_effect = _mock_fred_get_series
    mock_fred_cls.return_value = mock_fred

    count = collect_fred(db)
    assert count >= 1
    cursor = db.execute("SELECT COUNT(*) FROM sources WHERE source_type='fred'")
    assert cursor.fetchone()[0] >= 1


@patch("collector.fred.Fred")
def test_collect_fred_no_duplicates(mock_fred_cls, db):
    mock_fred = MagicMock()
    mock_fred.get_series.side_effect = _mock_fred_get_series
    mock_fred_cls.return_value = mock_fred

    collect_fred(db)
    count = collect_fred(db)
    assert count == 0


@patch("collector.fred.Fred")
def test_collect_fred_sets_domain_macro(mock_fred_cls, db):
    mock_fred = MagicMock()
    mock_fred.get_series.side_effect = _mock_fred_get_series
    mock_fred_cls.return_value = mock_fred

    collect_fred(db)
    cursor = db.execute("SELECT domain FROM sources WHERE source_type='fred' LIMIT 1")
    assert cursor.fetchone()[0] == "macro"
