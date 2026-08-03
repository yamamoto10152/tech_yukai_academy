# 【基本】演算子の使い方を体験しよう

print("Python" + "研修")        # → Python研修
print("ab" * 4)                 # → abababab
print(len("Hello"))             # → 5


# 【普通】変数と組み合わせてみよう

name = "山田"
print(name + "さんこんにちは")  # → 山田さんこんにちは

word = "Python"
print(len(word))                # → 6

age = 25
print("私は" + str(age) + "歳です")  # → 私は25歳です


# 【難しい】複数の操作を組み合わせてみよう

name = "山田"
age = 25
print(f"{name}さんは{age}歳です")    # → 山田さんは25歳です

text = "Python研修"
print(f"{text}の文字数は{len(text)}文字です")  # → Python研修の文字数は8文字です

print(len("Ha" * 5))            # → 10
