BASE_PAY = 1000


def calc_salary(hours, base_pay=BASE_PAY):
    return base_pay * hours


pay = calc_salary(160)
print("今月の給与：", pay, "円")
