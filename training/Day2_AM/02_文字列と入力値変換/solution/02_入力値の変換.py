"""
Day2: 入力値の変換（教材参考）
実行: python training/Day2_AM/02_文字列と入力値変換/solution/03_入力値の変換.py
"""

# str() … 数値などを文字列に変換
print(str(100))   # → 100

# int() … 文字列を整数に変換
print(int("100"))   # → 100

# float() … 文字列を小数に変換
print(float("3.14"))   # → 3.14


# 資料P35 演習の答え

age = 25
print("私は" + str(age) + "歳です")   # → 私は25歳です

price = "1000"
print(int(price) * 2)   # → 2000

print(f"私は{age}歳です")   # → 私は25歳です
