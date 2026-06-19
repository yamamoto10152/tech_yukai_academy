"""
Day3: 集合の基本（教材参考）
実行: python training/day03/ブール演算と集合/solution/02_集合の基本.py
"""

# 集合の作り方（重複は自動的に除かれる）

A = {1, 2, 3, 4}
B = set([1, 2, 2, 3, 3])
empty = set()

print(A)       # → {1, 2, 3, 4}
print(B)       # → {1, 2, 3}
print(empty)   # → set()


# 追加・削除・確認

A.add(5)
print(A)       # → {1, 2, 3, 4, 5}

A.remove(1)
print(A)       # → {2, 3, 4, 5}

print(3 in A)  # → True
print(9 in A)  # → False
