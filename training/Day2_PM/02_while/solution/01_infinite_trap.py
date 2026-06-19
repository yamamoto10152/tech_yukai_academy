print("--- 値の更新を忘れた例（無限ループになる。Ctrl+C で停止）---")
# count = 0
# while count < 3:
#     print("実行中")
#     # count += 1  ← これがないと永遠に続く

print("\n--- 正しい例（③で値を更新する）---")
count = 0
while count < 3:
    print("実行中")
    count += 1
