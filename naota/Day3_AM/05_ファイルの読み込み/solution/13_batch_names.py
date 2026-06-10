from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

with open(DATA / "names.txt", "r", encoding="utf-8") as f:
    names = f.readlines()

for name in names:
    print(f"宛名: {name.strip()} 様")

print(f"合計 {len(names)} 件のラベルを印刷します")
