"""
Day2: 文字列の基本（教材参考）
実行: python training/day02_am/文字列と入力値変換/solution/01_文字列の基本.py
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

name = "アシスト"
print(len(name))      # → 4
