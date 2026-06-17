scores = [80, 65, 90, 72]
total = 0

for score in scores:
    total += score

average = total / len(scores)
print(f"合計: {total}点")
print(f"平均: {average}点")
