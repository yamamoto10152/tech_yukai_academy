import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

with open(DATA / "members.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
