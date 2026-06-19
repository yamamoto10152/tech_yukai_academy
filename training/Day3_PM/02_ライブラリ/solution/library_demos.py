"""
Day3 午後：Pythonライブラリ（教材参考）
教材: yamamoto/Day3_PM.pdf

math / random / datetime の基本的な使い方です。
"""

import datetime
import math
import random


def demo_math() -> None:
    """import math → math.関数名()"""
    result = math.sqrt(16)
    print(result)  # 4.0


def demo_from_import() -> None:
    """from math import sqrt, pi → プレフィックスなしで使える"""
    from math import pi, sqrt

    print(sqrt(25))
    print(pi)


def demo_random() -> None:
    """random.randint / random.choice"""
    num = random.randint(1, 10)
    print("1〜10の乱数:", num)

    fruits = ["りんご", "バナナ", "みかん"]
    choice = random.choice(fruits)
    print("ランダム選択:", choice)


def demo_datetime() -> None:
    """現在日時・今日の日付"""
    now = datetime.datetime.now()
    print("現在日時:", now)

    today = datetime.date.today()
    print("今日の日付:", today)


def demo_alias() -> None:
    """import ... as ...（長い名前を短く）"""
    import datetime as dt

    print(dt.datetime.now())


if __name__ == "__main__":
    demo_math()
    demo_from_import()
    demo_random()
    demo_datetime()
    demo_alias()
