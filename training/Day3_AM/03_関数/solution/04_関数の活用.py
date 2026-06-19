"""
Day3: 関数の活用（教材参考）
実行: python training/day03/関数/solution/04_関数の活用.py
"""

# 関数を使うと同じ処理を何度も書かなくてよい


def tax_price(price):
    return price * 1.1


print(tax_price(1000))   # → 1100.0
print(tax_price(2000))   # → 2200.0
print(tax_price(3000))   # → 3300.0000000000005


# 挨拶と足し算の組み合わせ


def greet(name):
    print(f"{name}さん、こんにちは！")


def add(a, b):
    return a + b


greet("山田")              # → 山田さん、こんにちは！
print(add(10, 20))         # → 30
