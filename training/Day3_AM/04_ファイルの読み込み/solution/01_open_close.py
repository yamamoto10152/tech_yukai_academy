from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

f = open(DATA / "greet.txt", "r", encoding="utf-8")
content = f.read()
f.close()

print(content)
