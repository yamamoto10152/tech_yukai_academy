"""演習「ログ出力デコレーター」の完成例（教材 p.29）"""

from collections.abc import Callable
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def log_calls(func: F) -> F:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"{func.__name__}関数が実行されました")
        return func(*args, **kwargs)

    return wrapper  # type: ignore[return-value]


@log_calls
def sample_add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(sample_add(2, 3))
