"""
演習1: greet.txt を readlines で読む
data/greet.txt を readlines() で読み、各行を strip() して表示してください。

ヒント:
- with open(DATA / "greet.txt", "r", encoding="utf-8") as f:
- lines = f.readlines()
- for line in lines: print(line.strip())
"""

from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

# TODO: with と readlines で greet.txt を表示する
