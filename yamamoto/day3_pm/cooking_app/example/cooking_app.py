"""
Day3 午後：クッキングアプリケーション（総合演習）
教材: yamamoto/Day3_PM.pdf

例外処理・ライブラリ・デコレーター・クラスを組み合わせる演習です。
完成例は cooking_app/solution/cooking_app.py を参照してください。
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def cooking_timer(func: F) -> F:
    """TODO: cook の前後で経過時間を表示するデコレーターに仕上げる。

    ヒント:
      start = time.time()
      ... func を実行 ...
      end = time.time()
      print(f"調理にかかった時間: ...秒")
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError("演習: cooking_timer を実装してください")

    return wrapper  # type: ignore[return-value]


class SimpleDish:
    """TODO: 名前・材料・（任意で）手順リストを持ち、cook() で表示するクラス"""

    def __init__(self, name: str, ingredients: list[str], steps: list[str] | None = None) -> None:
        raise NotImplementedError("演習: SimpleDish.__init__")

    @cooking_timer
    def cook(self) -> None:
        # TODO: 手順を表示（time.sleep(0.2) などで「調理っぽさ」も演出してよい）
        raise NotImplementedError("演習: SimpleDish.cook")


def load_recipe_lines(filepath: str) -> list[str]:
    """演習: ファイルから行を読み込む（存在しなければ FileNotFoundError）。

    ヒント:
      - with open(filepath, encoding='utf-8') as f: が推奨
      - 呼び出し側で try-except FileNotFoundError する想定
    """
    raise NotImplementedError("演習: load_recipe_lines を実装してください")


def main() -> None:
    """TODO: SimpleDish のデモと、ファイル読込の try-except を組み合わせる。"""
    # TODO: SimpleDish を作って cook() を呼ぶ
    # TODO: load_recipe_lines(...) を try-except で呼ぶ
    # ヒント: 同じフォルダに recipe_sample.txt がある
    #   p = Path(__file__).with_name("recipe_sample.txt")
    #   lines = load_recipe_lines(str(p))
    print("演習を進めたら main() を完成させてください")


if __name__ == "__main__":
    main()
