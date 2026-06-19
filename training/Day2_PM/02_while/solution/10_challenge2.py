# 1. 1から n までの合計を while で求める
n = 10
total = 0
i = 1

while i <= n:
    total += i
    i += 1

print(f"1から{n}までの合計: {total}")

# 2. 7の倍数を探して break
target = 1
while target <= 50:
    if target % 7 == 0:
        print(f"最初の7の倍数: {target}")
        break
    target += 1

# 3. continue で偶数だけ表示
num = 0
while num < 6:
    num += 1
    if num % 2 == 1:
        continue
    print(f"偶数: {num}")
