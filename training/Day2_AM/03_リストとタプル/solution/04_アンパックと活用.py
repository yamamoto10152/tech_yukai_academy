"""
Day2: アンパックと活用（教材参考）
実行: python training/day02/リストとタプル/solution/04_アンパックと活用.py
"""

# タプルのアンパック：複数の変数に一気に代入

point = (35.6, 139.7)
lat, lng = point
print(lat)   # → 35.6
print(lng)   # → 139.7


# 3要素のアンパック

person = ("山田", 25, "東京")
name, age, city = person
print(name + "さんは" + city + "在住で" + str(age) + "歳です")
# → 山田さんは東京在住で25歳です


# タプルをリストに変換してから変更

person_list = list(person)
person_list[1] = 26
print(person_list)   # → ['山田', 26, '東京']
