# 【基本】

A = {1, 2, 3, 4}
print(A)
print(set([1, 2, 2, 3]))
print(set())


# 【普通】

A = {1, 2, 3}
A.add(4)
print(A)
A.remove(2)
print(A)
print(3 in A)


# 【難しい】

A = {1, 2, 3}
A.add(4)
A.remove(1)
print(A)

print(set(["東京", "大阪", "東京"]))
print(1 in {1, 2, 3})
print(9 in {1, 2, 3})
