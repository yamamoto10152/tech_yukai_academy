"""
チャレンジアップ 01: global を使わない給与計算
BASE_PAY を定数として使い、引数と return で給与を計算してください。

ヒント:
- def calc_salary(hours, base_pay=BASE_PAY):
- return base_pay * hours
"""

BASE_PAY = 1000

# TODO: calc_salary を引数・return で書く

pay = calc_salary(160)
print("今月の給与：", pay, "円")
