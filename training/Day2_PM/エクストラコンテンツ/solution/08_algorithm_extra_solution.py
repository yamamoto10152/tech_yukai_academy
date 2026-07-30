# Day2 extra contents - solution 8
# アルゴリズム チャレンジ問題の回答

# Challenge 1:
# 次のリストから、最大値と最小値を両方求めて表示してください。
values = [12, 45, 7, 33, 56, 21]
max_value = values[0]
min_value = values[0]

for value in values[1:]:
    if value > max_value:
        max_value = value
    if value < min_value:
        min_value = value

print(f'最大値: {max_value}')
print(f'最小値: {min_value}')

print('---')

# Challenge 2:
# 線形探索を使って、target が何番目にあるかを表示してください。
# 見つからなければ「見つかりませんでした」と表示してください。
numbers = [8, 3, 15, 6, 10, 21]
target = 10
found = False

for i, num in enumerate(numbers):
    if num == target:
        print(f'{target} は {i} 番目にあります')
        found = True
        break

if not found:
    print('見つかりませんでした')

print('---')

# Challenge 3:
# 次の得点リストの平均点を求め、平均点以上の人だけを表示してください。
scores = [('田中', 72), ('鈴木', 88), ('佐藤', 65), ('山田', 91), ('高橋', 84)]

total = 0
for name, score in scores:
    total += score

average = total / len(scores)
print(f'平均点: {average:.1f}')

for name, score in scores:
    if score >= average:
        print(f'平均点以上: {name}（{score}点）')
