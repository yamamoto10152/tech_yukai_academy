"""演習「入力値の例外処理」の完成例（教材 p.11）"""


def exercise_double_input() -> None:
    user_input = input("数値を入力してください: ")
    try:
        n = int(user_input)
        print(n * 2)
    except ValueError:
        print("正しい数値を入力してください")


if __name__ == "__main__":
    exercise_double_input()
