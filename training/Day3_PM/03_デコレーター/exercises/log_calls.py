"""
Day3 午後：デコレーター（演習）
教材: yamamoto/Day3_PM.pdf p.29

問題:
  関数が呼び出されたときに
  「〇〇関数が実行されました」と表示するデコレーターを作る。
  （〇〇は実際の関数名）

ヒント:
  - func.__name__ で関数名（文字列）が取れる
  - wrapper の中で print() する
  - 引数のある関数にも対応したい場合は *args, **kwargs を使う

完成例は 03_decorators/solution/log_calls.py を参照してください。
"""

from collections.abc import Callable
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def log_calls(func: F) -> F:
    """TODO: 呼び出しログを出すデコレーターを完成させる"""

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # TODO: f"{func.__name__}関数が実行されました" のように表示
        # TODO: そのあと func(*args, **kwargs) を return する

    return wrapper  # type: ignore[return-value]


@log_calls
def sample_add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    # 実装後にコメントを外して確認
    # print(sample_add(2, 3))
    print("log_calls を実装してから sample_add(2, 3) を呼び出してください")
