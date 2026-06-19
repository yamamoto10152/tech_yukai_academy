prices = [120, 250, 300, 80]
max_price = prices[0]

for p in prices:
    if p > max_price:
        max_price = p

print(f"最高価格は {max_price} 円です")
