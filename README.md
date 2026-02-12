# Hello AI Dev - Python Hello World

このリポジトリは、**Pythonをはじめて触る人向け**の最小アプリです。  
「プログラムを実行すると文字が表示される」という基本を体験できます。

## できること

このアプリを実行すると、ターミナルに次の1行が表示されます。

```text
Hello, World!
```

## ファイル構成

```text
.
├── app.py     # Hello, World! を表示するプログラム
└── README.md  # この説明書
```

## 事前準備

- Python 3.8 以上（推奨）

Python が入っているか確認するには、次を実行します。

```bash
python3 --version
```

## 実行方法（3ステップ）

1. このリポジトリに移動する
   ```bash
   cd /workspace/hello-ai-dev
   ```
2. アプリを実行する
   ```bash
   python3 app.py
   ```
3. `Hello, World!` と表示されたら成功です。

## コードの読み方（初心者向け）

`app.py` の重要なポイントは次のとおりです。

- `def main()`: 処理をまとめる「関数」を作っています。
- `print("Hello, World!")`: 文字を画面に表示します。
- `if __name__ == "__main__":`: このファイルを直接実行したときだけ `main()` を動かします。

## よくあるエラー

- `python3: command not found`
  - Python が未インストールの可能性があります。Python をインストールしてください。
- `can't open file 'app.py'`
  - 実行場所が違う可能性があります。`cd /workspace/hello-ai-dev` で移動してから再実行してください。

## 次の練習

`print("Hello, World!")` を次のように変えて、表示が変わるか試してみましょう。

```python
print("こんにちは、Python!")
```
