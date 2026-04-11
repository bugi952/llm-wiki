from unittest.mock import patch, MagicMock
import pytest
from db import get_db, init_db
from collector.manual import process_input, _convert_x_url


@pytest.fixture
def db():
    conn = get_db(":memory:")
    init_db(conn)
    yield conn
    conn.close()


def test_convert_x_url():
    assert _convert_x_url("https://x.com/user/status/123") == "https://fxtwitter.com/user/status/123"
    assert _convert_x_url("https://twitter.com/user/status/456") == "https://fxtwitter.com/user/status/456"
    assert _convert_x_url("https://example.com/page") == "https://example.com/page"


def test_process_input_url(db):
    source_id = process_input(db, "https://anthropic.com/blog/new-feature")
    assert source_id is not None
    cursor = db.execute("SELECT source_type, status, url FROM sources WHERE id=?", (source_id,))
    row = cursor.fetchone()
    assert row[0] == "manual"
    assert row[1] == "collected"
    assert row[2] == "https://anthropic.com/blog/new-feature"


def test_process_input_x_url(db):
    source_id = process_input(db, "https://x.com/karpathy/status/12345")
    cursor = db.execute("SELECT url FROM sources WHERE id=?", (source_id,))
    # URL stored as original, but content should use fxtwitter
    assert cursor.fetchone()[0] == "https://x.com/karpathy/status/12345"


def test_process_input_text(db):
    source_id = process_input(db, "Claude 5 출시 예정. 성능 2배 향상.")
    cursor = db.execute("SELECT source_type, title, content FROM sources WHERE id=?", (source_id,))
    row = cursor.fetchone()
    assert row[0] == "manual"
    assert "Claude 5" in row[1]
    assert "Claude 5" in row[2]


def test_process_input_text_with_url(db):
    source_id = process_input(db, "이거 봐 https://openai.com/gpt5 엄청나다")
    cursor = db.execute("SELECT url FROM sources WHERE id=?", (source_id,))
    assert cursor.fetchone()[0] == "https://openai.com/gpt5"


def test_process_input_no_duplicate(db):
    process_input(db, "https://anthropic.com/blog/new-feature")
    source_id = process_input(db, "https://anthropic.com/blog/new-feature")
    assert source_id is None  # duplicate
