"""
チャレンジアップ 02: 設定ファイルの読み込み
data/settings.txt を読み、key=value 形式を辞書に入れて表示してください。

期待する出力の例:
theme: dark
language: ja
max_users: 100

ヒント:
- line.strip().split("=") で key と value に分ける
- settings[key] = value
"""

from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

# TODO: settings.txt を読み辞書にして3項目を print する
