from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

with open(DATA / "greet.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    print(line.strip())
