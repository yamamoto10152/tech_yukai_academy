# Day2 extra contents - solution 3
# ランダム処理を使ってみよう

import random

# Q1: サイコロを作る
result = random.randint(1, 6)
print(f'サイコロの目: {result}')

# Q2: おすすめ観光地を選ぶ
spots = ['京都', '大阪', '東京', '北海道', '沖縄']
pick = random.choice(spots)
print(f'おすすめ観光地: {pick}')

# Q3: カードをシャッフルする
cards = ['A', 'B', 'C', 'D', 'E']
random.shuffle(cards)
print(cards)
