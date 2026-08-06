"""追加問題「ファイルから Recipe を組み立てる」の完成例"""

from __future__ import annotations

import datetime
from pathlib import Path


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


def recipe_from_file(filepath: str) -> Recipe:
    with open(filepath, encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f if line.strip() and not line.startswith("#")]

    name = lines[0]
    ingredients: list[str] = []
    for line in lines[1:]:
        if line.startswith("材料:"):
            ingredients.append(line.split(":", 1)[1].strip())

    return Recipe(name, ingredients)


def main() -> None:
    recipe_path = Path(__file__).resolve().parents[1] / "exercises" / "recipe_sample.txt"
    recipe = recipe_from_file(str(recipe_path))
    recipe.show_recipe()


if __name__ == "__main__":
    main()
