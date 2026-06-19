PASS_SCORE = 60
TAX_RATE = 0.10


def judge(score):
    if score >= PASS_SCORE:
        return "合格"
    return "不合格"


def calc_price(price):
    return price + price * TAX_RATE


scores = [72, 55, 88]
for s in scores:
    print(s, "点 →", judge(s))

print("税込価格:", calc_price(1000), "円")
