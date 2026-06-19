import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

with open(DATA / "scores.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(row[0], "さんの点数は", row[1], "点です")
