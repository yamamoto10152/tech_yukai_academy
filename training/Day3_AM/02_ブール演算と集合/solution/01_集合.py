"""
Day3: 集合（教材参考）
実行: python training/Day3_AM/02_ブール演算と集合/solution/01_集合.py
"""

# ブール演算（資料P14〜16）

print(10 > 5)      # → True
print(10 == 10)    # → True
print(10 > 20 and 5 < 10)   # → False


# 集合の基本（資料P18〜19）

A = {1, 2, 3, 4}
print(3 in A)      # → True


# 資料P22 演習の答え

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A & B)   # → {4, 5}
print(A | B)   # → {1, 2, 3, 4, 5, 6, 7, 8}
print(A - B)   # → {1, 2, 3}

data = ["東京", "大阪", "東京", "名古屋", "大阪"]
print(set(data))
