# 【基本】


def greet(name):
    print(f"{name}さん、こんにちは！")


greet("山田")


def show_pair(a, b):
    print(a, b)


show_pair(10, 20)
greet("佐藤")


# 【普通】


def add_print(a, b):
    print(a + b)


add_print(10, 20)


def show_input(text):
    print(f"入力: {text}")


show_input("sample")


# 【難しい】


def show_three(a, b, c):
    print(a, b, c)


show_three(1, 2, 3)


def double(n):
    print(n * 2)


double(5)
double(10)


def report(name, score):
    print(f"{name}: {score}")


report("山田", 85)
