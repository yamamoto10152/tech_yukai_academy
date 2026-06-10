count = 0

while count < 5:
    count += 1
    if count == 3:
        print("スキップします")
        continue
    print(count)

# 出力: 1, 2, スキップします, 4, 5（3は表示されない）
