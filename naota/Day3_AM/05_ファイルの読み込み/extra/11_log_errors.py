"""
チャレンジアップ 01: ログ解析
data/access.log を読み、「ERROR」を含む行だけ表示し、
最後に ERROR の件数を表示してください。

ヒント:
- if "ERROR" in line:
- error_count を数える
"""

from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
error_count = 0

# TODO: access.log を読み ERROR 行を表示・件数を数える
