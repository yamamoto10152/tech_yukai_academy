# 【基本】

print(str(100))
print(int("50"))
print(float("2.5"))


# 【普通】

age = 25
print("年齢は" + str(age) + "歳")

price = "800"
print(int(price) + 200)

# print("100" + 100)  # → TypeError


# 【難しい】

a = "10"
b = "20"
print(int(a) + int(b))

rate = "0.1"
print(float(rate) * 1000)

# int("Hello")  # → ValueError
