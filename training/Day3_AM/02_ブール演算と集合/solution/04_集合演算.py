# 【基本】

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A & B)
print(A | B)
print(A - B)


# 【普通】

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A & B)
print(A | B)
print(A - B)
print(set([1, 1, 2, 2, 3]))
print({1, 2, 3} - {2, 3, 4})


# 【難しい】

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A & B)
print(A | B)
print(A - B)
print(3 in A and 5 in A)
print(set([1, 2]) & set([2, 3]))
