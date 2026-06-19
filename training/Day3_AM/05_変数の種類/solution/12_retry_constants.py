MAX_RETRY = 3
WAIT_SECONDS = 5

for attempt in range(1, MAX_RETRY + 1):
    print(f"試行 {attempt}/{MAX_RETRY}（{WAIT_SECONDS}秒待機想定）")

print("リトライ上限に達しました")
