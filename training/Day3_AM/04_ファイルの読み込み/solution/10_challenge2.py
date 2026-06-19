from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

total = 0

with open(DATA / "sales.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    month, amount = line.strip().split(",")
    total += int(amount)
    print(f"{month}: {amount}円")

print(f"売上合計: {total}円")
