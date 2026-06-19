"""
Day3 午後：機械学習基礎（解答）
教材: yamamoto/Day3_numpy_pandas_ml.pdf p.25-28

身長から体重を予測する線形回帰モデルのデモ。
"""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def main() -> None:
    # 身長(cm)
    X = np.array([155, 160, 165, 170, 175, 180, 185]).reshape(-1, 1)
    # 体重(kg)
    y = np.array([50, 55, 58, 65, 68, 72, 78])

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


if __name__ == "__main__":
    main()
