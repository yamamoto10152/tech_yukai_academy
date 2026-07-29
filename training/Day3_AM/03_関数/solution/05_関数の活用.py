# 【基本】


def greet(name):
    print(f"{name}さん、こんにちは！")


greet("山田")


def add(a, b):
    return a + b


print(add(10, 20))


def tax_price(price):
    return price * 1.1


print(tax_price(500))


# 【普通】

print(tax_price(1000))
print(tax_price(2000))
print(tax_price(3000))


def format_id(user_id):
    return f"user_{user_id}"


print(format_id(42))


# 【難しい】


def greet(name):
    print(f"{name}さん、こんにちは！")


def add(a, b):
    return a + b


def tax_price(price):
    return price * 1.1


greet("山田")
print(add(10, 20))
print(tax_price(1000))


def tax_price_v2(price):
    return price * 1.08


print(tax_price_v2(1000))
print(tax_price_v2(2000))


def double(n):
    return n * 2


print(double(add(5, 10)))
