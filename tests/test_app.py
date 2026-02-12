"""Flask アプリの基本動作を確認するテスト。"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app


def test_root_returns_hello_world() -> None:
    """トップページが期待どおりの文字列を返すことを確認する。"""
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hello World"
