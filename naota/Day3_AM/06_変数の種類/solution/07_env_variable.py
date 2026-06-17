import os

# 環境変数がなければデフォルト値を使う（学習用）
app_lang = os.environ.get("APP_LANG", "ja")
api_key = os.environ.get("API_KEY", "（未設定）")

print("言語設定:", app_lang)
print("APIキー:", api_key)
