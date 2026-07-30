"""
Day2: リスト（教材参考）
実行: python training/Day2_AM/03_リストとタプル/solution/01_リスト.py
"""

# リストの作り方：[ ] で囲み、カンマで区切る

names = ["田中", "佐藤", "山田"]
print(names[0])   # → 田中
print(len(names)) # → 3


# 書き換えと追加

fruits = ["りんご", "バナナ", "みかん"]
fruits[1] = "ぶどう"
fruits.append("もも")
print(fruits)     # → ['りんご', 'ぶどう', 'みかん', 'もも']


# 資料P46 演習の答え

foods = ["カレー", "ラーメン", "寿司"]
print(foods)
print(len(foods))
print(foods[0])
foods[1] = "うどん"
print(foods)
foods.append("そば")
print(foods)
