"""
Day2: タプル（教材参考）
実行: python training/day02/リストとタプル/solution/03_タプル.py
"""

# タプルの作り方：( ) で囲み、カンマで区切る

point = (35.6, 139.7)
rgb = (255, 128, 0)
person = ("山田", 25, "東京")

print(point)      # → (35.6, 139.7)
print(rgb)        # → (255, 128, 0)
print(person)     # → ('山田', 25, '東京')


# インデックスと長さ（リストと同じ使い方）

print(point[0])   # → 35.6
print(len(point)) # → 2


# タプルは変更できない（実行すると TypeError）
# point[0] = 0.0
