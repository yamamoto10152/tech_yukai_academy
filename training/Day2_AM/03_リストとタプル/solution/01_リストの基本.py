"""
Day2: リストの基本（教材参考）
実行: python training/day02/リストとタプル/solution/01_リストの基本.py
"""

# リストの作り方：[ ] で囲み、カンマで区切る

names = ["田中", "佐藤", "山田"]
scores = [80, 95, 72, 88]
mixed = ["山田", 25, True]
empty = []

print(names)    # → ['田中', '佐藤', '山田']
print(scores)   # → [80, 95, 72, 88]
print(mixed)    # → ['山田', 25, True]
print(empty)    # → []


# インデックスで要素を取り出す（0始まり）

print(names[0])   # → 田中
print(names[1])   # → 佐藤
print(names[2])   # → 山田


# リストの長さ

print(len(names))    # → 3
print(len(scores))   # → 4
