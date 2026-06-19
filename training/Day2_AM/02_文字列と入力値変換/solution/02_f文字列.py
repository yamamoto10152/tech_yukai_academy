"""
Day2: f文字列（教材参考）
実行: python training/day02_am/文字列と入力値変換/solution/02_f文字列.py
"""

# f"" の中に {変数} を書くと、変数を文字列に埋め込める

name = "山田"
age = 25
print(f"{name}さんは{age}歳です")   # → 山田さんは25歳です


# 従来の書き方（str() が必要）
print(name + "さんは" + str(age) + "歳です")   # → 山田さんは25歳です
