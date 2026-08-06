"""追加問題「正しい数値が入力されるまで繰り返す」の完成例"""


def retry_until_valid() -> None:
    while True:
        user_input = input("数値を入力してください: ")
        try:
            n = int(user_input)
            print(f"入力値: {n}")
            break
        except ValueError:
            print("もう一度")


if __name__ == "__main__":
    retry_until_valid()
