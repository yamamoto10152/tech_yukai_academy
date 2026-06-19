"""
Day3: 戻り値（教材参考）
実行: python training/day03/関数/solution/03_戻り値.py
"""

# return で結果を返す


def add(a, b):
    return a + b


result = add(10, 20)
print(result)       # → 30
print(result * 2)   # → 60


# 税込価格を計算する関数


def tax_price(price):
    return price * 1.1


print(tax_price(1000))   # → 1100.0
