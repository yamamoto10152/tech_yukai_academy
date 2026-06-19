"""
Day3 午後：モデル評価（解答）
教材: yamamoto/Day3_numpy_pandas_ml.pdf p.25-30

勉強時間→点数の予測とMSE・R²による評価のデモ。
"""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


def main() -> None:
    # 特徴量（勉強時間）
    X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
    # 正解ラベル（テスト点数）
    y = np.array([30, 40, 50, 55, 65, 70, 80, 85])

    # データ分割
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=0
    )

    # モデル作成・学習
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 予測
    y_pred = model.predict(X_test)
    print("予測値:", y_pred)
    print("実際の値:", y_test)

    # MSE（平均二乗誤差）: 小さいほど良い
    mse = mean_squared_error(y_test, y_pred)
    print(f"MSE: {mse:.2f}")

    # R²（決定係数）: 1に近いほど良い
    r2 = model.score(X_test, y_test)
    print(f"R²: {r2:.4f}")

    # 新しいデータの予測
    prediction = model.predict([[10]])
    print(f"10時間勉強した場合の予測点数: {prediction[0]:.1f}")


if __name__ == "__main__":
    main()
