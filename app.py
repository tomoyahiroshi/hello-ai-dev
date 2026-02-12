"""Flask を使ったシンプルな Hello World Web アプリ。"""

from flask import Flask

app = Flask(__name__)


@app.get("/")
def hello() -> str:
    """トップページで挨拶を返します。"""
    return "Hello World"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
