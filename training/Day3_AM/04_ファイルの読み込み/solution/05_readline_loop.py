from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

with open(DATA / "greet.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()
