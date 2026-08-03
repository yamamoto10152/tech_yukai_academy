# 【基本】

price = "1000"
print(int(price) * 2)

age = 25
print(f"私は{age}歳です")

print(str(500) + "円")


# 【普通】

qty = "3"
unit = "150"
print(int(qty) * int(unit))

score = 85
print("score: " + str(score))

value = "3.14"
print(float(value) * 2)


# 【難しい】

name = "山田"
age = 25
print(name + "さんは" + str(age) + "歳です")
print(f"{name}さんは{age}歳です")

base = "1000"
rate = "0.08"
print(float(base) * float(rate))

# print("100" + 100)  # → TypeError
print(int("100") + 100)  # → 200
