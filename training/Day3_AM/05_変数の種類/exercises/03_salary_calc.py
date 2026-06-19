"""
演習2: 給与計算（定数と global）
① BASE_PAY = 1000（定数・大文字）
② calc_salary(hours) で global BASE_PAY を使い給与を計算

期待する出力: 今月の給与： 160000 円

ヒント:
- ① BASE_PAY = 1000
- ② global BASE_PAY
- salary = BASE_PAY * hours / return salary
"""

# TODO: BASE_PAY と calc_salary を書く

pay = calc_salary(160)
print("今月の給与：", pay, "円")
