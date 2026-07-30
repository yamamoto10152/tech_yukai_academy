# Day2 extra contents - extra 1
# range チャレンジ問題

# Challenge 1:
# 1〜30 の中で「3 の倍数かつ偶数」の数だけを表示してください。
# 期待する出力: 6, 12, 18, 24, 30
for i in range(1, 31):
    if i % 3 == 0 and i % 2 == 0:
        print(i)

print('---')

# Challenge 2:
# 20 から 1 までカウントダウンしながら、5 の倍数だけを表示してください。
# ヒント: range の step に注目
for i in range(20, 0, -1):
    if i % 5 == 0:
        print(i)

print('---')

# Challenge 3:
# 1〜50 の中で 4 の倍数をすべて足した合計を表示してください。
# ヒント: total を用意して、for 文の中で足していく

total = 0
for i in range(4, 51, 4):
    total += i

print(f'合計: {total}')
