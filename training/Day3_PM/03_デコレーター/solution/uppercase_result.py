"""追加問題「戻り値を大文字にするデコレーター」の完成例"""

from collections.abc import Callable
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., str])


def uppercase(func: F) -> F:
    def wrapper(*args: Any, **kwargs: Any) -> str:
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper  # type: ignore[return-value]


@uppercase
def greet(name: str) -> str:
    return f"hello, {name}"


if __name__ == "__main__":
    print(greet("taro"))  # HELLO, TARO
