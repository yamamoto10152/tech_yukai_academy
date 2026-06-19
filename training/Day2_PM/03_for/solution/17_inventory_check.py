products = ["牛乳", "パン", "ヨーグルト"]
expired = ["パン"]

print("--- 在庫チェック ---")
for item in products:
    if item in expired:
        print(f"{item}: 期限切れです")
    else:
        print(f"{item}: OK")
