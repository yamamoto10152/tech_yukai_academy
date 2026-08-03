"""
Day2: 文字列（教材参考）
実行: python training/Day2_AM/02_文字列と入力値変換/solution/01_文字列.py
"""

# 文字列は "" か '' で囲む（どちらも同じ意味）

print("Hello")   # → Hello
print('Hello')   # → Hello


# + で連結、* で繰り返し

print("Hello" + "World")   # → HelloWorld
print("Ha" * 3)            # → HaHaHa


# len() で文字数を調べる

print(len("Hello"))   # → 5
print(len("山田"))    # → 2


# f文字列

name = "山田"
age = 25
print(f"{name}さんは{age}歳です")   # → 山田さんは25歳です


# 資料P30 演習の答え

name = "山田"
food = "カレー"
print(f"{name}の好きな食べ物は{food}です")
print("Ha" * 5)
print(len(name))
