"""
Day3: 引数（教材参考）
実行: python training/day03/関数/solution/02_引数.py
"""

# 引数あり：渡した値に応じて処理が変わる


def greet(name):
    print(f"{name}さん、こんにちは！")


greet("山田")   # → 山田さん、こんにちは！
greet("佐藤")   # → 佐藤さん、こんにちは！


# 引数が2つ


def add(a, b):
    print(a + b)


add(10, 20)   # → 30
