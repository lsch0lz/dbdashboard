import pytest

from controller.database import get_conn

def test_get_conn():
    conn = get_conn()
    assert conn.is_connected() == True