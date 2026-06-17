"""
Day3 午後：クッキングアプリ（教材参考）
教材: yamamoto/Day3_PM.pdf p.47

Recipe クラスの完成例です。
"""

import datetime


class Recipe:
    def __init__(self, name: str, ingredients: list[str]) -> None:
        self.name = name
        self.ingredients = ingredients
        self.created_at = datetime.datetime.now()

    def show_recipe(self) -> None:
        print(f"レシピ: {self.name}")
        print("材料:")
        for ing in self.ingredients:
            print(f"  - {ing}")
        print(f"作成日時: {self.created_at}")


if __name__ == "__main__":
    demo = Recipe("カレー", ["肉", "野菜", "カレールー"])
    demo.show_recipe()
