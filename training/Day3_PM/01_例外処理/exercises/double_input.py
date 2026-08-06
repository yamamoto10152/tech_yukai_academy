"""
Day3 午後：例外処理（演習）
教材: yamamoto/Day3_PM.pdf p.11

問題:
  ユーザーから数値を入力してもらい、その数値を2倍にして表示する。
  数値以外が入力されたときは「正しい数値を入力してください」と表示する。

ヒント:
  - int() で変換できないと ValueError が発生する
  - try / except ValueError: でキャッチする

完成例は exceptions/solution/double_input.py を参照してください。
"""


def exercise_double_input() -> None:
    user_input = input("数値を入力してください: ")

    # TODO: try / except で数値化し、2倍した値を print する
    XXX:
        n = int(user_input)
        # TODO: n * 2 を表示
        pass
    XXX ValueError:
        print("正しい数値を入力してください")


if __name__ == "__main__":
    exercise_double_input()
