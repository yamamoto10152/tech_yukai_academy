"""
Day3: 関数の活用（追加問題・任意）解答
在庫確認システムを関数で作るシナリオです
"""

# ========================================
# 問題1: 在庫確認関数を作ろう
# ========================================
def check_stock(order):
    if 10 >= order:
        print("注文OK")
    else:
        print("在庫不足")

check_stock(3)   # → 注文OK
check_stock(15)  # → 在庫不足


# ========================================
# 問題2: 注文可能かをreturnで返そう
# ========================================
def can_order(stock, order):
    return stock >= order

result = can_order(10, 3)
print(result)  # → True

result = can_order(2, 5)
print(result)  # → False


# ========================================
# 問題3: 複数商品に使い回してみよう
# ========================================
def can_order(stock, order):
    return stock >= order

products = [
    ("Oracle", 10, 3),
    ("Zabbix", 2, 5),
    ("Linux", 8, 8),
]

for name, stock, order in products:
    if can_order(stock, order):
        print(f"{name}: 注文OK")
    else:
        print(f"{name}: 在庫不足")


# ========================================
# 問題4: 在庫数を更新する関数を作ろう
# ========================================
def update_stock(stock, order):
    return stock - order

result = update_stock(10, 3)
print(result)  # → 7


# ========================================
# 問題5: 一連の処理を組み合わせよう
# ========================================
def can_order(stock, order):
    return stock >= order

def update_stock(stock, order):
    return stock - order

stock = 10
order = 3

if can_order(stock, order):
    remaining = update_stock(stock, order)
    print(f"注文完了。残り在庫: {remaining}個")
else:
    print("在庫不足。注文できません")