"""
Day3 午後：機械学習基礎（追加演習）
教材: yamamoto/Day3_numpy_pandas_ml.pdf p.25-30

問題:
  勉強時間からテスト点数を予測するモデルを作成し、精度を評価する。
  1. データの分割を行う
  2. LinearRegression で学習・予測
  3. MSE（平均二乗誤差）と R²（決定係数）を計算して表示
  4. 新しいデータ（勉強時間=10時間）の点数を予測する

ヒント:
  - from sklearn.metrics import mean_squared_error
  - mse = mean_squared_error(y_test, y_pred)
  - r2 = model.score(X_test, y_test)
  - model.predict([[10]]) で新データの予測

完成例は 08_machine_learning/solution/model_evaluation.py を参照してください。
"""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


def train_and_evaluate():
    """勉強時間→点数の予測モデルを学習し、評価指標を表示する。"""
    # 特徴量（勉強時間）
    X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
    # 正解ラベル（テスト点数）
    y = np.array([30, 40, 50, 55, 65, 70, 80, 85])

    # TODO: train_test_split で分割
    raise NotImplementedError("演習: データ分割を実装してください")

    # TODO: モデル作成・学習・予測
    raise NotImplementedError("演習: モデルの学習と予測を実装してください")

    # TODO: MSE を計算
    # mse = mean_squared_error(y_test, y_pred)
    raise NotImplementedError("演習: MSEの計算を実装してください")

    # TODO: R² を計算
    # r2 = model.score(X_test, y_test)
    raise NotImplementedError("演習: R²の計算を実装してください")

    print(f"MSE: {mse}")
    print(f"R²: {r2}")

    # TODO: 勉強時間10時間の予測
    # prediction = model.predict([[10]])
    raise NotImplementedError("演習: 新データの予測を実装してください")

    print(f"10時間勉強した場合の予測点数: {prediction[0]:.1f}")


if __name__ == "__main__":
    train_and_evaluate()
