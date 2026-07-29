"""
Day3: 関数（教材参考）
実行: python training/Day3_AM/03_関数/solution/01_関数.py
"""

# 関数の定義と呼び出し


def greet():
    print("こんにちは！")


greet()   # → こんにちは！


# 引数


def greet(name):
    print(f"{name}さん、こんにちは！")


greet("山田")   # → 山田さん、こんにちは！


# 戻り値


def add(a, b):
    return a + b


print(add(10, 20))   # → 30


# 資料P30 演習の答え


def greet(name):
    print(f"{name}さん、こんにちは！")


greet("山田")


def add(a, b):
    return a + b


result = add(10, 20)
print(result)   # → 30


def tax_price(price):
    return price * 1.1


print(tax_price(1000))   # → 1100.0
