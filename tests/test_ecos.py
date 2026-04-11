from unittest.mock import patch, MagicMock
import pytest
from db import get_db, init_db
from collector.ecos import collect_ecos


@pytest.fixture(autouse=True)
def set_ecos_key(monkeypatch):
    monkeypatch.setenv("ECOS_API_KEY", "test-key")


@pytest.fixture
def db():
    conn = get_db(":memory:")
    init_db(conn)
    yield conn
    conn.close()


FAKE_ECOS_RESPONSE = {
    "StatisticSearch": {
        "row": [
            {"STAT_NAME": "기준금리", "TIME": "202603", "DATA_VALUE": "3.25"},
        ]
    }
}


@patch("collector.ecos.requests.get")
def test_collect_ecos_inserts(mock_get, db):
    resp = MagicMock()
    resp.raise_for_status = MagicMock()
    resp.json.return_value = FAKE_ECOS_RESPONSE
    mock_get.return_value = resp

    count = collect_ecos(db)
    assert count >= 1
    cursor = db.execute("SELECT domain FROM sources WHERE source_type='ecos' LIMIT 1")
    assert cursor.fetchone()[0] == "macro"


@patch("collector.ecos.requests.get")
def test_collect_ecos_no_duplicates(mock_get, db):
    resp = MagicMock()
    resp.raise_for_status = MagicMock()
    resp.json.return_value = FAKE_ECOS_RESPONSE
    mock_get.return_value = resp

    collect_ecos(db)
    count = collect_ecos(db)
    assert count == 0
