from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
error_count = 0

with open(DATA / "access.log", "r", encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line:
            error_count += 1
            print(line.strip())

print(f"ERROR の件数: {error_count} 件")
