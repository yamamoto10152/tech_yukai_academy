"""
演習4: sales.txt の合計
data/sales.txt を読み、各行の売上を表示したあと合計金額を表示してください。

sales.txt の形式: 月,金額（例: 1月,150000）

ヒント:
- line.strip().split(",") で月と金額に分ける
- int(amount) で数値に変換して total に足す
"""

from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
total = 0

# TODO: readlines で sales.txt を読み、合計を計算する
