"""
Day3 午後：クラス（教材参考）
教材: yamamoto/Day3_PM.pdf

class / __init__ / self / クラス変数 / 継承の例です。
"""


class Dog:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def bark(self) -> None:
        print(f"{self.name}がワンワン！")


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def introduce(self) -> None:
        print(f"私は{self.name}、{self.age}歳です")


class Counter:
    """クラス変数 total とインスタンス変数 id の例"""

    total: int = 0

    def __init__(self) -> None:
        Counter.total += 1
        self.id = Counter.total


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> None:
        print("何か鳴く")


class Cat(Animal):
    def speak(self) -> None:
        print(f"{self.name}がニャー")


if __name__ == "__main__":
    d = Dog("ポチ", 3)
    d.bark()

    p = Person("花子", 20)
    p.introduce()

    c1, c2 = Counter(), Counter()
    print(f"Counter id: {c1.id}, {c2.id}, total={Counter.total}")

    cat = Cat("ミケ")
    cat.speak()
