"""
Day2: 型変換の応用（教材参考）
実行: python training/day02_am/文字列と入力値変換/solution/04_型変換の応用.py
"""

# 文字列を数値に変換して計算
price = "1000"
print(int(price) * 2)   # → 2000


# f文字列なら str() なしで書ける
age = 25
print(f"私は{age}歳です")   # → 私は25歳です


# よくあるエラー（実行するとエラーになる）
# int("Hello")      # → ValueError（数字以外は整数に変換できない）
# print("100" + 100)  # → TypeError（文字列と数値は + でつなげない）
