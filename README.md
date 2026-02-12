# Hello AI Dev - Flask Hello World

このリポジトリは、**Flask を使った最小の Web アプリ**です。  
ブラウザで `Hello World` を表示する基本を体験できます。

## できること

アプリを起動してブラウザでアクセスすると、次の文字が表示されます。

```text
Hello World
```

## ファイル構成

```text
.
├── app.py     # Flask で Hello World を返す Web アプリ
└── README.md  # この説明書
```

## 事前準備

- Python 3.8 以上（推奨）
- Flask

Python が入っているか確認するには、次を実行します。

```bash
python3 --version
```

Flask が未インストールの場合は、次でインストールしてください。

```bash
pip install flask
```

## 実行方法

1. このリポジトリに移動する
   ```bash
   cd /workspace/hello-ai-dev
   ```
2. アプリを起動する
   ```bash
   python3 app.py
   ```
3. ブラウザで次へアクセスする
   ```text
   http://127.0.0.1:5000
   ```
4. `Hello World` が表示されたら成功です。

## コードの読み方（初心者向け）

`app.py` の重要なポイントは次のとおりです。

- `app = Flask(__name__)`: Flask アプリ本体を作成します。
- `@app.get("/")`: `/` へのアクセスを処理するルートを定義します。
- `return "Hello World"`: ブラウザに表示する文字列を返します。
- `app.run(...)`: 開発用サーバーを起動します。

## よくあるエラー

- `ModuleNotFoundError: No module named 'flask'`
  - Flask が未インストールです。`pip install flask` を実行してください。
- `Address already in use`
  - 5000 番ポートが使われています。別プロセスを停止するか、ポート番号を変更してください。
