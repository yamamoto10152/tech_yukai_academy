"""
Day2: 変数の活用（教材参考）
実行: python training/day02_am/if/solution/04_変数の活用.py
"""

# 同じ値を変数に入れると、直す場所が1か所で済む

name = "山田"
print(name + "さん")              # → 山田さん
print(name + "さんの点数")        # → 山田さんの点数
print(name + "さんへようこそ")    # → 山田さんへようこそ


# 箱の中身を変えると、式の結果もまとめて変わる

tax_rate = 0.10
price = 1000
tax = price * tax_rate
total = price + tax
print("税抜:", price)    # → 税抜: 1000
print("税額:", tax)      # → 税額: 100.0
print("税込:", total)    # → 税込: 1100.0


# 数値は str() で文字列にしてから + する

name = "山田"
age = 25
print(name + "さんは" + str(age) + "歳です")   # → 山田さんは25歳です
