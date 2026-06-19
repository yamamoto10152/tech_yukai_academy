"""
Day2: リストの操作（教材参考）
実行: python training/day02/リストとタプル/solution/02_リストの操作.py
"""

# 要素の書き換えと追加

items = ["A", "B", "C"]
items[1] = "D"
print(items)          # → ['A', 'D', 'C']

items.append("E")
print(items)          # → ['A', 'D', 'C', 'E']


# 要素の削除と取り出し

items.remove("D")
print(items)          # → ['A', 'C', 'E']

item = items.pop()
print(item)           # → E
print(items)          # → ['A', 'C']
