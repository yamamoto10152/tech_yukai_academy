"""
演習2: fruit.txt を読む
data/fruit.txt を読み、各行を表示してください。

期待する出力:
りんご
みかん
ぶどう
バナナ

ヒント:
- ① 読み込みモード "r"
- ② 全行をリストで読むメソッド readlines()
"""

from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

# TODO: with open(DATA / "fruit.txt", "r", encoding="utf-8") as f:
# TODO:     lines = f.readlines()
# TODO: for line in lines: print(line.strip())
