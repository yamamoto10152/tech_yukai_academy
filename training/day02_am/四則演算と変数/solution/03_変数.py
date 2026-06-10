"""
Day2: 変数（教材参考）
実行: python training/day02_am/if/solution/03_変数.py
"""

# 変数は名前のついた箱。= は「右の値を左に入れる」

name = "山田"
score = 100
print(name)    # → 山田
print(score)   # → 100


# 再代入（上書き）

score = 50
print(score)   # → 50

score = 100
print(score)   # → 100


# 自分自身を使った更新

count = 0
count = count + 1
print(count)   # → 1
