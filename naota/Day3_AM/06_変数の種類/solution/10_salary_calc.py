BASE_PAY = 1000


def calc_salary(hours):
    global BASE_PAY
    salary = BASE_PAY * hours
    return salary


pay = calc_salary(160)
print("今月の給与：", pay, "円")
