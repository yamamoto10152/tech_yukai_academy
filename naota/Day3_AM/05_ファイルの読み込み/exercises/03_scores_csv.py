"""
演習3: scores.csv を読む
各行の「名前」と「点数」を表示してください。

期待する出力:
田中 さんの点数は 85 点です
佐藤 さんの点数は 92 点です
鈴木 さんの点数は 78 点です

ヒント:
- reader = csv.reader(f)
- next(reader) でヘッダーを読み飛ばす
- 名前は row[0]、点数は row[1]
"""

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

# TODO: with open と csv.reader、next(reader)、for row in reader で表示する
