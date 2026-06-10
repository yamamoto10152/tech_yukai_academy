"""
Day3: ブール演算（教材参考）
実行: python training/day03/ブール演算と集合/solution/01_ブール演算.py
"""

# 比較演算子（結果は True または False）

print(10 > 5)      # → True
print(10 == 10)    # → True
print(10 != 5)     # → True
print(80 >= 60)    # → True
print(3 < 1)       # → False


# and（両方 True のとき True）

print(10 > 5 and 5 < 10)    # → True
print(10 > 20 and 5 < 10)   # → False


# or（どちらか True のとき True）

print(10 > 20 or 5 < 10)    # → True


# not（条件を反転）

print(not False)   # → True
print(not (10 > 20))   # → True
