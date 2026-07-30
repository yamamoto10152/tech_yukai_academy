# 【基本】

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A & B)
print(3 in A)
print(10 > 5 and 3 in A)


# 【普通】

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A & B)
print(A | B)
print(A - B)
print(len(set(["a", "a", "b", "c"])))
nums = {2, 4, 6, 8}
print(4 in nums and 5 in nums)


# 【難しい】

# ブール演算は条件の判定、集合演算はデータの抽出

A = {1, 2, 3}
B = {3, 4, 5}
print(len(A | B))
print(1 in A or 9 in A)
print(1 in A and 2 in A)
