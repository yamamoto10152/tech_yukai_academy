"""
Day3: keys・values・items（教材参考）
実行: python training/day03/辞書型/solution/03_keysとitems.py
"""

person = {"name": "山田", "age": 25, "dept": "営業部"}

print(person.keys())     # → dict_keys(['name', 'age', 'dept'])
print(person.values())   # → dict_values(['山田', 25, '営業部'])


# items() と for 文で全要素を表示

for key, value in person.items():
    print(f"{key}：{value}")
# → name：山田
# → age：25
# → dept：営業部
