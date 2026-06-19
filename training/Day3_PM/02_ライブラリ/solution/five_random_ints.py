"""演習「ランダム整数5個」の完成例（教材 p.21）"""

import random


def exercise_five_random_ints() -> None:
    for _ in range(5):
        print(random.randint(1, 100))


if __name__ == "__main__":
    exercise_five_random_ints()
