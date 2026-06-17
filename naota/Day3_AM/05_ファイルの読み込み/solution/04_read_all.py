from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

with open(DATA / "greet.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("--- 全体を1つの文字列で受け取る ---")
print(repr(content))
