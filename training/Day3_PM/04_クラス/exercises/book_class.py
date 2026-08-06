"""
Day3 午後：クラス（演習）
教材: yamamoto/Day3_PM.pdf p.39

問題:
  書籍を表す Book クラスを作る。
  属性: title（タイトル）, author（著者）, price（価格）
  メソッド: show_info() で情報を表示

ヒント:
  - __init__ で self.title などに代入
  - show_info() 内で print、f文字列が便利

完成例は classes/solution/book_class.py を参照してください。
"""


class Book:
    """TODO: このクラスを完成させる"""

    def __init__(self, title: str, author: str, price: int) -> None:
        # TODO: 3つの属性を self に保存

    def show_info(self) -> None:
        # TODO: f"『{self.title}』 / 著者: {self.author} / 価格: {self.price}円"の形で表示


if __name__ == "__main__":
    # b = Book("Python入門", "山田", 1980)
    # b.show_info()
    print("Book クラスを実装してから上のコメントを外して実行してください")
