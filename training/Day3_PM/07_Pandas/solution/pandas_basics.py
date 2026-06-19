"""
Day3 午後：Pandas基礎（解答）
教材: yamamoto/Day3_numpy_pandas_ml.pdf p.11-16

Series・DataFrameの作成、データ確認、フィルタリングのデモ。
"""
import pandas as pd


def main() -> None:
    # --- Series ---
    s = pd.Series([170, 165, 180, 155],
                  index=["田中", "佐藤", "鈴木", "高橋"])
    print("=== Series ===")
    print(s)

    # --- DataFrame ---
    data = {
        "名前": ["田中", "佐藤", "鈴木", "高橋", "伊藤"],
        "年齢": [25, 30, 22, 35, 28],
        "部署": ["営業", "開発", "営業", "開発", "人事"],
    }
    df = pd.DataFrame(data)
    print("\n=== DataFrame ===")
    print(df)

    # データ確認メソッド
    print("\n=== head() ===")
    print(df.head())
    print("\n=== info() ===")
    df.info()
    print("\n=== describe() ===")
    print(df.describe())
    print("\n=== shape ===")
    print(df.shape)

    # --- 演習: フィルタリング ---
    # 問題1: 年齢が25以上
    print("\n=== 年齢25以上 ===")
    print(df[df["年齢"] >= 25])

    # 問題2: 部署が"開発"
    print("\n=== 開発部 ===")
    print(df[df["部署"] == "開発"])

    # 問題3: 年齢の平均
    print("\n=== 平均年齢 ===")
    print(df["年齢"].mean())  # 28.0


if __name__ == "__main__":
    main()
