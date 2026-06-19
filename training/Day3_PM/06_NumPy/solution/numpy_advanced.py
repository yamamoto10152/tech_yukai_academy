"""
Day3 午後：NumPy応用（解答）
教材: yamamoto/Day3_numpy_pandas_ml.pdf p.5-7

NumPyの配列生成関数と演算の応用デモ。
"""
import numpy as np


def generate_evens() -> np.ndarray:
    """0〜100の偶数だけの配列を返す（0含む、100含まない）。"""
    return np.arange(0, 100, 2)


def sin_wave(n_points: int = 100) -> tuple[np.ndarray, np.ndarray]:
    """0〜2*piをn_points分割し、(x配列, sin(x)配列)のタプルを返す。"""
    x = np.linspace(0, 2 * np.pi, n_points)
    y = np.sin(x)
    return x, y


def mean_absolute_difference(a: np.ndarray, b: np.ndarray) -> float:
    """2つの配列の要素ごとの差の絶対値の平均を返す。"""
    return float(np.mean(np.abs(a - b)))


def main() -> None:
    evens = generate_evens()
    print("偶数配列:", evens)

    x, y = sin_wave()
    print(f"sin波: x={x[:3]}..., y={y[:3]}...")

    a = np.array([10, 20, 30, 40, 50])
    b = np.array([12, 18, 33, 37, 55])
    print("平均絶対差:", mean_absolute_difference(a, b))  # 3.4


if __name__ == "__main__":
    main()
