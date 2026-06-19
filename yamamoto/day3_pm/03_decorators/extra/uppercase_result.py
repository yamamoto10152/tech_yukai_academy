"""
追加問題: 戻り値を大文字にするデコレーター

問題:
  文字列を返す関数に付けて、戻り値を .upper() した結果を返すデコレーターを作る。

ヒント:
  - def uppercase(func): ... の形でよい
  - wrapper 内で result = func(*args, **kwargs) としてから変換
"""

from collections.abc import Callable
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., str])


def uppercase(func: F) -> F:
    # TODO: 実装
    raise NotImplementedError("追加問題を実装してください")


@uppercase
def greet(name: str) -> str:
    return f"hello, {name}"


if __name__ == "__main__":
    # 実装後: print(greet("taro"))  → "HELLO, TARO"
    pass
