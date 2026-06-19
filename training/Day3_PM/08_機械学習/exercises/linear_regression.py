"""
Day3 午後：機械学習基礎（演習）
教材: yamamoto/Day3_numpy_pandas_ml.pdf p.27

問題:
  身長データから体重を予測する線形回帰モデルを作成する。
  1. train_test_split でデータを学習用75%・テスト用25%に分割
  2. LinearRegression でモデルを作成・学習
  3. テストデータで予測を行う

ヒント:
  - train_test_split(X, y, test_size=0.25, random_state=0)
  - model = LinearRegression() → model.fit(X_train, y_train)
  - y_pred = model.predict(X_test)

完成例は 08_machine_learning/solution/linear_regression.py を参照してください。
"""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def predict_weight():
    """身長から体重を予測するモデルを学習し、予測結果を表示する。"""
    # 身長(cm)
    X = np.array([155, 160, 165, 170, 175, 180, 185]).reshape(-1, 1)
    # 体重(kg)
    y = np.array([50, 55, 58, 65, 68, 72, 78])

    # TODO: train_test_split でデータを分割（test_size=0.25, random_state=0）
    # X_train, X_test, y_train, y_test = ...
    raise NotImplementedError("演習: train_test_split を使ってデータを分割してください")

    # TODO: LinearRegression モデルを作成して学習
    # model = ...
    # model.fit(...)
    raise NotImplementedError("演習: モデルの作成と学習を実装してください")

    # TODO: テストデータで予測
    # y_pred = ...
    raise NotImplementedError("演習: predict で予測してください")

    print("予測値:", y_pred)
    print("実際の値:", y_test)


if __name__ == "__main__":
    predict_weight()
