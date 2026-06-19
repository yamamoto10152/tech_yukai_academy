"""
Day3 午後：Pandas応用（解答）
教材: yamamoto/Day3_numpy_pandas_ml.pdf p.11-15

列の追加、複数条件フィルタリング、統計情報のデモ。
"""
import pandas as pd


def main() -> None:
    data = {
        "名前": ["田中", "佐藤", "鈴木", "高橋", "伊藤"],
        "数学": [80, 65, 90, 70, 85],
        "英語": [70, 85, 75, 60, 90],
    }
    df = pd.DataFrame(data)

    # 合計点列を追加
    df["合計"] = df["数学"] + df["英語"]
    print("=== 合計点追加後 ===")
    print(df)

    # 合計150以上
    print("\n=== 合計150以上 ===")
    print(df[df["合計"] >= 150])

    # 数学80以上 & 英語70以上
    print("\n=== 数学80以上 & 英語70以上 ===")
    print(df[(df["数学"] >= 80) & (df["英語"] >= 70)])

    # 統計情報
    print("\n=== 統計情報 ===")
    print(df.describe())


if __name__ == "__main__":
    main()
