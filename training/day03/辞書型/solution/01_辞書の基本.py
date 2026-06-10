"""
Day3: 辞書の基本（教材参考）
実行: python training/day03/辞書型/solution/01_辞書の基本.py
"""

# 辞書の作り方：{ Key: Value } のペア

person = {
    "name": "山田",
    "age": 25,
    "dept": "営業部",
}
scores = {"math": 80, "english": 95, "science": 72}
empty = {}

print(person)    # → {'name': '山田', 'age': 25, 'dept': '営業部'}
print(scores)    # → {'math': 80, 'english': 95, 'science': 72}
print(empty)     # → {}


# Key を指定して Value を取り出す

print(person["name"])   # → 山田
print(person["age"])    # → 25
print(person["dept"])   # → 営業部
