"""
Day2: タプルとリスト（教材参考）
実行: python training/Day2_AM/03_リストとタプル/solution/02_タプルとリスト.py
"""

# タプルのアンパック

person = ("山田", 25, "東京")
name, age, city = person
print(name + "さんは" + city + "在住で" + str(age) + "歳です")


# タプルをリストに変換してから変更

person_list = list(person)
person_list[1] = 26
print(person_list)   # → ['山田', 26, '東京']


# 資料P52 演習の答え

person = ("山田", 25, "東京")
name, age, city = person
print(f"{name}さんは{city}在住で{age}歳です")

person_list = list(person)
person_list[1] = 26
print(person_list)
