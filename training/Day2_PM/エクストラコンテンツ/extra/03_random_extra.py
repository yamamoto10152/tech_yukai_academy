# Day2 extra contents - extra 3
# random チャレンジ問題

import random

# Challenge 1:
# メンバーの中から重複なしで 3 人選び、「今日の当番: [...]」と表示してください。
members = ['田中', '鈴木', '佐藤', '山田', '高橋']
chosen = random.sample(members, 3)
print(f'今日の当番: {chosen}')

print('---')

# Challenge 2:
# 1〜20 のランダムな整数を 5 つ作り、その中で 10 以上の数だけ表示してください。
nums = []
for _ in range(5):
    nums.append(random.randint(1, 20))

print(f'生成された数: {nums}')
for n in nums:
    if n >= 10:
        print(f'10以上: {n}')

print('---')

# Challenge 3:
# メニューをシャッフルして、先頭の 2 つを「おすすめセット」として表示してください。
menu = ['カレー', 'ラーメン', 'パスタ', 'うどん', 'そば']
random.shuffle(menu)
print(f'おすすめセット: {menu[:2]}')
