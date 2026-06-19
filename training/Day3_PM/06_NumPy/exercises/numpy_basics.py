"""
Day3 午後：NumPy基礎（演習）
教材: yamamoto/Day3_numpy_pandas_ml.pdf p.8

問題:
  テストの点数データに対して以下の操作を行う。
  1. 全員に5点加算した結果を表示
  2. 平均点を求める
  3. 最高点と最低点を求める

ヒント:
  - np.array() でリストをNumPy配列に変換
  - 配列 + 数値 でブロードキャスト（一括加算）
  - np.mean(), np.max(), np.min() で統計量を計算

完成例は 06_NumPy/solution/numpy_basics.py を参照してください。
"""
import numpy as np


def score_analysis(scores_list: list[int]) -> dict:
    """点数データを分析して結果を辞書で返す。

    Returns:
        {"added": 5点加算後の配列, "mean": 平均, "max": 最高点, "min": 最低点}
    """
    scores = np.array(scores_list)

    # TODO: scores に 5 を加算した配列を added に代入
    added = None
    raise NotImplementedError("演習: 5点加算を実装してください")

    # TODO: 平均点を計算
    mean_score = None
    raise NotImplementedError("演習: 平均点の計算を実装してください")

    # TODO: 最高点・最低点を計算
    max_score = None
    min_score = None
    raise NotImplementedError("演習: 最高点・最低点の計算を実装してください")

    return {"added": added, "mean": mean_score, "max": max_score, "min": min_score}


if __name__ == "__main__":
    result = score_analysis([65, 80, 55, 90, 72])
    print("5点加算:", result["added"])
    print("平均点:", result["mean"])
    print("最高点:", result["max"])
    print("最低点:", result["min"])
