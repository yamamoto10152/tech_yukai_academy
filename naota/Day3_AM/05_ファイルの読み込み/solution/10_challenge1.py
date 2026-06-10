import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

print("--- greet.txt ---")
with open(DATA / "greet.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        print(line.strip())

print("\n--- scores.csv ---")
with open(DATA / "scores.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(row[0], "さんの点数は", row[1], "点です")

print("\n--- sales.txt 合計 ---")
total = 0
with open(DATA / "sales.txt", "r", encoding="utf-8") as f:
    for line in f:
        _, amount = line.strip().split(",")
        total += int(amount)
print(f"売上合計: {total}円")
