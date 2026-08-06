"""追加問題「Person を継承した Student クラス」の完成例"""


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def introduce(self) -> None:
        print(f"私は{self.name}、{self.age}歳です")


class Student(Person):
    def __init__(self, name: str, age: int, grade: int) -> None:
        super().__init__(name, age)
        self.grade = grade

    def introduce(self) -> None:
        print(f"私は{self.name}、{self.age}歳、{self.grade}年生です")


if __name__ == "__main__":
    s = Student("太郎", 15, 2)
    s.introduce()
