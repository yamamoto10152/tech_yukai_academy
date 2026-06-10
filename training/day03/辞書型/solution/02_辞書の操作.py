"""
Day3: 辞書の操作（教材参考）
実行: python training/day03/辞書型/solution/02_辞書の操作.py
"""

# 追加（存在しない Key に代入）

person = {"name": "山田", "age": 25}
person["dept"] = "営業部"
print(person)   # → {'name': '山田', 'age': 25, 'dept': '営業部'}


# 更新（存在する Key に再代入）

person["age"] = 26
print(person)   # → {'name': '山田', 'age': 26, 'dept': '営業部'}


# 存在しない Key はエラー（実行すると KeyError）
# print(person["email"])
