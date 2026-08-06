"""追加問題「今日の日付をフォーマットして表示」の完成例"""

import datetime


def format_today() -> None:
    today = datetime.date.today()
    print(today.strftime("%Y年%m月%d日"))


if __name__ == "__main__":
    format_today()
