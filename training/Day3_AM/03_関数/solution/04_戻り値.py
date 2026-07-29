# 【基本】


def add(a, b):
    return a + b


print(add(10, 20))

result = add(10, 20)
print(result)


def tax_price(price):
    return price * 1.1


print(tax_price(1000))


# 【普通】

print(add(10, 20) * 2)


def subtract(a, b):
    return a - b


print(subtract(20, 8))


# 【難しい】

print(tax_price(1000))
print(tax_price(2000))
print(tax_price(3000))

total = add(10, 20) + 5
print(total)


def multiply(a, b):
    return a * b


print(add(10, 20) + multiply(2, 3))
