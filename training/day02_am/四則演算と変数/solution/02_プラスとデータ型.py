"""
Day2: 「+」とデータ型（教材参考）
実行: python training/day02_am/if/solution/02_プラスとデータ型.py
"""

# 文字列（str）同士 → 連結
print("Hello" + "World")   # → HelloWorld

# 数値（int）同士 → 足し算
print(100 + 200)           # → 300

# 型が違うと + はエラー（実行すると TypeError）
# print(100 + "行")

# 数値を文字列に変換してからつなげる
print(str(25) + "歳")      # → 25歳
