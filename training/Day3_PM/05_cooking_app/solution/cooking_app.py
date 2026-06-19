"""
クッキングアプリ総合演習の完成例
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def cooking_timer(func: F) -> F:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"調理にかかった時間: {elapsed:.2f}秒")
        return result

    return wrapper  # type: ignore[return-value]


class SimpleDish:
    def __init__(self, name: str, ingredients: list[str], steps: list[str] | None = None) -> None:
        self.name = name
        self.ingredients = ingredients
        self.steps = steps or []

    @cooking_timer
    def cook(self) -> None:
        print(f"=== {self.name} を調理します ===")
        print("材料:")
        for ing in self.ingredients:
            print(f"  - {ing}")
        print("手順:")
        for i, step in enumerate(self.steps, start=1):
            print(f"  {i}. {step}")
            time.sleep(0.2)
        print("完成！")


def load_recipe_lines(filepath: str) -> list[str]:
    with open(filepath, encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f if line.strip() and not line.startswith("#")]


def main() -> None:
    dish = SimpleDish(
        "オムレツ",
        ["卵 2個", "牛乳 100ml"],
        ["ボウルで混ぜる", "弱火で加熱する"],
    )
    dish.cook()

    recipe_path = Path(__file__).with_name("recipe_sample.txt")
    try:
        lines = load_recipe_lines(str(recipe_path))
        print("\n--- ファイルから読み込んだレシピ ---")
        for line in lines:
            print(line)
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {recipe_path}")


if __name__ == "__main__":
    main()
