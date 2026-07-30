# 【基本】

items = ["X", "Y", "Z"]
items[1] = "W"
print(items)

items = ["X", "Y", "Z"]
items.append("END")
print(items)

items = ["X", "Y", "Z"]
items.remove("Y")
print(items)


# 【普通】

items = ["A", "B", "C"]
item = items.pop()
print(item)
print(items)

items = ["A", "B", "C"]
items[1] = "D"
items.append("E")
items.remove("A")
print(items)

items = ["A", "B", "C"]
print(len(items))
items.append("D")
print(len(items))
items.pop()
print(len(items))


# 【難しい】

items = [1, 2, 3, 4]
items.pop(0)
print(items)

items = ["A"]
items.append("B")
items.append("C")
items.append("D")
items.remove("B")
print(items)

items = ["A", "B", "C"]
items[1] = "X"
items.pop()
print(items)
