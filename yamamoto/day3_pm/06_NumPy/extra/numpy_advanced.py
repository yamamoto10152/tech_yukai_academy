"""
Day3 午後：NumPy基礎（追加演習）
教材: yamamoto/Day3_numpy_pandas_ml.pdf p.5-7

問題:
  NumPyの便利な配列生成とブロードキャストを活用した応用問題。
  1. np.arange() を使って 0〜100 の偶数だけの配列を作る
  2. np.linspace() を使って 0〜2*pi を100分割した配列を作り、
     np.sin() で正弦波を計算する
  3. 2つの配列の要素ごとの差を計算し、差の絶対値の平均を求める

ヒント:
  - np.arange(start, stop, step)
  - np.linspace(start, stop, num)
  - np.abs() で絶対値、np.mean() で平均

完成例は 06_NumPy/solution/numpy_advanced.py を参照してください。
"""
import numpy as np


def generate_evens() -> np.ndarray:
    """0〜100の偶数だけの配列を返す（0含む、100含まない）。"""
    # TODO: np.arange() を使って実装
    raise NotImplementedError("演習: 偶数配列を生成してください")


def sin_wave(n_points: int = 100) -> tuple[np.ndarray, np.ndarray]:
    """0〜2*piをn_points分割し、(x配列, sin(x)配列)のタプルを返す。"""
    # TODO: np.linspace() と np.sin() を使って実装
    raise NotImplementedError("演習: 正弦波を生成してください")


def mean_absolute_difference(a: np.ndarray, b: np.ndarray) -> float:
    """2つの配列の要素ごとの差の絶対値の平均を返す。"""
    # TODO: np.abs() と np.mean() を組み合わせて実装
    raise NotImplementedError("演習: 平均絶対差を計算してください")


if __name__ == "__main__":
    evens = generate_evens()
    print("偶数配列:", evens)

    x, y = sin_wave()
    print(f"sin波: x={x[:3]}..., y={y[:3]}...")

    a = np.array([10, 20, 30, 40, 50])
    b = np.array([12, 18, 33, 37, 55])
    print("平均絶対差:", mean_absolute_difference(a, b))
