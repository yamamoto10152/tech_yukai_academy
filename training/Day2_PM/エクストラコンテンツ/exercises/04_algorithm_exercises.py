# Day2 extra contents - exercises 4
# アルゴリズムを実装しよう

import random

# Q1: 1〜10 のランダムな整数を 5 つ生成してリストに入れ、
#     そのリストの合計値と平均値を表示してください。
nums = []
for i in range(???):
    nums.append(random.randint(???, ???))

total = ???
print(f'リスト: {nums}')
print(f'合計: {total}  平均: {total / len(nums):.1f}')

print('---')

# Q2: 以下のリストで enumerate を使いながら最小値とその位置を探してください。
temps = [23, 18, 31, 15, 27, 19]
min_temp = temps[0]
min_index = 0

for i, temp in enumerate(temps):
    if ???:
        min_temp = ???
        min_index = ???

print(f'最低気温: {min_temp}度（{min_index}番目）')
