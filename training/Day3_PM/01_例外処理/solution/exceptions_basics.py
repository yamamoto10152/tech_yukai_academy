"""
Day3 午後：例外処理（教材参考）
教材: yamamoto/Day3_PM.pdf

try / except / else / finally の基本パターンです。
そのまま実行して挙動を確認してください。
"""


def demo_zero_division() -> None:
    """ゼロ除算をキャッチする例"""
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("ゼロで割ることはできません")
    else:
        # エラーが起きなかったときだけ実行
        print(result)


def demo_multiple_except() -> None:
    """複数の except（上から順に最初にマッチしたものだけ）"""
    try:
        num = int(input("数字を入力: "))
        result = 100 / num
        print(result)
    except ValueError:
        print("数字を入力してください")
    except ZeroDivisionError:
        print("ゼロでは割れません")


def demo_finally() -> None:
    """finally はエラーの有無にかかわらず実行される"""
    try:
        file = open("data.txt", "r", encoding="utf-8")
        content = file.read()
        file.close()
        print(content)
    except FileNotFoundError:
        print("ファイルが見つかりません")
    finally:
        print("処理を終了します")


if __name__ == "__main__":
    demo_zero_division()
    # demo_multiple_except()
    # demo_finally()
