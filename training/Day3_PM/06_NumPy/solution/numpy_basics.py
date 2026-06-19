"""
Day3 午後：NumPy基礎（解答）
教材: yamamoto/Day3_numpy_pandas_ml.pdf p.5-9

NumPyの配列作成・ブロードキャスト・統計関数のデモ。
"""
import numpy as np


def main() -> None:
    # --- 配列の作成 ---
    a = np.array([1, 2, 3, 4, 5])
    print("配列:", a)
    print("型:", type(a))

    # --- 便利な配列生成 ---
    zeros = np.zeros(5)
    ones = np.ones(3)
    rng = np.arange(0, 10, 2)
    lin = np.linspace(0, 1, 5)
    print(f"zeros: {zeros}")
    print(f"ones: {ones}")
    print(f"arange: {rng}")
    print(f"linspace: {lin}")

    # --- ブロードキャスト演算 ---
    a = np.array([10, 20, 30, 40, 50])
    print(f"a + 5 = {a + 5}")
    print(f"a * 2 = {a * 2}")
    print(f"a / 10 = {a / 10}")

    # --- 演習: テストの点数 ---
    scores = np.array([65, 80, 55, 90, 72])

    # 問題1: 全員に5点加算
    print("5点加算:", scores + 5)  # [70 85 60 95 77]

    # 問題2: 平均点
    print("平均点:", np.mean(scores))  # 72.4

    # 問題3: 最高点・最低点
    print("最高点:", np.max(scores))  # 90
    print("最低点:", np.min(scores))  # 55


if __name__ == "__main__":
    main()
