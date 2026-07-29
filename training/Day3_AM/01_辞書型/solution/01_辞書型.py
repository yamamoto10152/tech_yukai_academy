"""
Day3: 辞書型（教材参考）
実行: python training/Day3_AM/01_辞書型/solution/01_辞書型.py
"""

# 辞書の作り方：{ Key: Value } のペア

person = {
    "name": "山田",
    "age": 25,
    "dept": "営業部",
}
scores = {"math": 80, "english": 95, "science": 72}

print(person["name"])   # → 山田
print(person["age"])    # → 25


# 追加・更新

person = {"name": "山田", "age": 25}
person["dept"] = "営業部"
person["age"] = 26
print(person)


# keys() / values() / items()

for key, value in person.items():
    print(f"{key}：{value}")


# 資料P11 演習の答え

profile = {
    "name": "山田",
    "age": 25,
    "hobby": "読書",
}
print(f'名前：{profile["name"]}')
print(f'趣味：{profile["hobby"]}')
profile["dept"] = "開発部"
print(profile)
for key, value in profile.items():
    print(f"{key}：{value}")
