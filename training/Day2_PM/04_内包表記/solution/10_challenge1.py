fruits = ["apple", "banana", "cherry", "grape", "mango"]
sales = [500, 1200, 800, 1500, 300, 2000, 950, 1100]

fruits_result = [fruit.upper() for fruit in fruits if "a" in fruit]
sales_result = [str(s) + "円" for s in sales if s >= 1000]
even_double = [n * 2 for n in range(1, 11) if n % 2 == 0]

print("果物:", fruits_result)
print("売上:", sales_result)
print("偶数の2倍:", even_double)
