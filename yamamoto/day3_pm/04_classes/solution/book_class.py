"""演習「Bookクラス」の完成例（教材 p.39）"""


class Book:
    def __init__(self, title: str, author: str, price: int) -> None:
        self.title = title
        self.author = author
        self.price = price

    def show_info(self) -> None:
        print(f"『{self.title}』 / 著者: {self.author} / 価格: {self.price}円")


if __name__ == "__main__":
    b = Book("Python入門", "山田", 1980)
    b.show_info()
