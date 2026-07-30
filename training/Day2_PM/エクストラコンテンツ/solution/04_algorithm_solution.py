# Day2 extra contents - solution 4
# アルゴリズムを実装しよう

import random

# Q1: ランダムリストの合計・平均
nums = []
for i in range(5):
    nums.append(random.randint(1, 10))

total = sum(nums)
print(f'リスト: {nums}')
print(f'合計: {total}  平均: {total / len(nums):.1f}')

print('---')

# Q2: enumerate で最小値を探す
temps = [23, 18, 31, 15, 27, 19]
min_temp = temps[0]
min_index = 0

for i, temp in enumerate(temps):
    if temp < min_temp:
        min_temp = temp
        min_index = i

print(f'最低気温: {min_temp}度（{min_index}番目）')
