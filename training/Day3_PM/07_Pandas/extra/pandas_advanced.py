"""
Day3 午後：Pandas基礎（追加演習）
教材: yamamoto/Day3_numpy_pandas_ml.pdf p.11-15

問題:
  成績データのDataFrameを作成し、以下の操作を行う。
  1. 数学と英語の合計点列を追加する
  2. 合計点が150以上の生徒を抽出する
  3. 数学が80以上かつ英語が70以上の生徒を抽出する（複数条件）
  4. df.describe() で統計情報を表示する

ヒント:
  - df["新列名"] = df["列A"] + df["列B"] で列追加
  - 複数条件: df[(条件1) & (条件2)]
  - df.describe() で統計量一覧

完成例は 07_Pandas/solution/pandas_advanced.py を参照してください。
"""
import pandas as pd


def create_scores_df() -> pd.DataFrame:
    """成績データのDataFrameを返す。"""
    data = {
        "名前": ["田中", "佐藤", "鈴木", "高橋", "伊藤"],
        "数学": [80, 65, 90, 70, 85],
        "英語": [70, 85, 75, 60, 90],
    }
    return pd.DataFrame(data)


def add_total_column(df: pd.DataFrame) -> pd.DataFrame:
    """数学と英語の合計点列 "合計" を追加したDataFrameを返す。"""
    # TODO: df["合計"] = df["数学"] + df["英語"] のように実装
    raise NotImplementedError("演習: 合計点列の追加を実装してください")


def filter_high_total(df: pd.DataFrame, threshold: int = 150) -> pd.DataFrame:
    """合計点が threshold 以上の行を返す。"""
    # TODO: df[df["合計"] >= threshold] で実装
    raise NotImplementedError("演習: 合計点フィルタを実装してください")


def filter_multi_condition(df: pd.DataFrame) -> pd.DataFrame:
    """数学が80以上かつ英語が70以上の行を返す。"""
    # TODO: df[(df["数学"] >= 80) & (df["英語"] >= 70)] で実装
    raise NotImplementedError("演習: 複数条件フィルタを実装してください")


if __name__ == "__main__":
    df = create_scores_df()
    print("=== 成績データ ===")
    print(df)

    df = add_total_column(df)
    print("\n=== 合計点追加後 ===")
    print(df)

    print("\n=== 合計150以上 ===")
    print(filter_high_total(df))

    print("\n=== 数学80以上 & 英語70以上 ===")
    print(filter_multi_condition(df))

    print("\n=== 統計情報 ===")
    print(df.describe())
