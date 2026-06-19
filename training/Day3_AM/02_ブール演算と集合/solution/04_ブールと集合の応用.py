"""
Day3: ブールと集合の応用（教材参考）
実行: python training/day03/ブール演算と集合/solution/04_ブールと集合の応用.py
"""

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A & B)   # 両方に含まれる → {4, 5}
print(A | B)   # どちらかに含まれる → {1, 2, 3, 4, 5, 6, 7, 8}
print(A - B)   # AにあってBにない → {1, 2, 3}


# ブール演算と in の組み合わせ

nums = {2, 4, 6, 8}
print(4 in nums and 5 in nums)   # → False
print(4 in nums or 5 in nums)    # → True
