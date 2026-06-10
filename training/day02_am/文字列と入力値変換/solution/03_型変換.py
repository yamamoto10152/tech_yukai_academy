"""
Day2: 型変換（教材参考）
実行: python training/day02_am/文字列と入力値変換/solution/03_型変換.py
"""

# 型が違うデータを + でつなぐとエラーになる
# age = 25
# print("私は" + age + "歳です")   # → TypeError


# str() … 数値などを文字列に変換
print(str(100))   # → 100


# int() … 文字列を整数に変換
print(int("100"))   # → 100


# float() … 文字列を小数に変換
print(float("3.14"))   # → 3.14


# str() を使って連結
age = 25
print("私は" + str(age) + "歳です")   # → 私は25歳です
