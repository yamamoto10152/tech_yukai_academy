"""
Day3 午後：デコレーター（教材参考）
教材: yamamoto/Day3_PM.pdf

関数の前後に処理を足すパターンと、*args / **kwargs の形です。
"""

import time
from collections.abc import Callable
from typing import Any


def my_decorator(func: Callable[[], None]) -> Callable[[], None]:
    def wrapper() -> None:
        print("関数の前に実行")
        func()
        print("関数の後に実行")

    return wrapper


@my_decorator
def say_hello() -> None:
    print("Hello!")


def timer(func: Callable[[], None]) -> Callable[[], None]:
    """実行時間を測るデコレーター（引数なし関数向けの簡易版）"""

    def wrapper() -> None:
        start = time.time()
        func()
        end = time.time()
        print(f"実行時間: {end - start:.4f}秒")

    return wrapper


@timer
def slow_function() -> None:
    time.sleep(0.3)
    print("処理完了")


def repeat(num: int) -> Callable[[Callable[..., None]], Callable[..., None]]:
    """引数あり関数向け（教材 p.28）— *args, **kwargs の形"""

    def decorator(func: Callable[..., None]) -> Callable[..., None]:
        def wrapper(*args: Any, **kwargs: Any) -> None:
            for _ in range(num):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greet(name: str) -> None:
    print(f"こんにちは、{name}さん")


if __name__ == "__main__":
    say_hello()
    slow_function()
    greet("太郎")
