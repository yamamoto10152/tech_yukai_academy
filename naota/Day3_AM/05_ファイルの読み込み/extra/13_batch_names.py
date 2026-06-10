"""
チャレンジアップ 03: 一括処理（名前リスト）
data/names.txt を読み、「宛名: ○○ 様」と表示し、
最後に件数を表示してください。

ヒント:
- readlines() で名前リストを取得
- len(names) で件数
"""

from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

# TODO: names.txt を読みラベル形式で表示する
