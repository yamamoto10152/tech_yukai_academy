"""
Day3 午後：Pandas基礎（演習）
教材: yamamoto/Day3_numpy_pandas_ml.pdf p.16

問題:
  社員データのDataFrameを作成し、以下の操作を行う。
  1. 年齢が25以上の人を抽出
  2. 部署が"開発"の人を抽出
  3. 年齢の平均を求める

ヒント:
  - pd.DataFrame(辞書) で表を作成
  - df[df["列名"] >= 値] で条件フィルタリング
  - df["列名"] == "文字列" で文字列の一致条件
  - df["列名"].mean() で平均を計算

完成例は 07_Pandas/solution/pandas_basics.py を参照してください。
"""
import pandas as pd


def create_employee_df() -> pd.DataFrame:
    """社員データのDataFrameを返す。"""
    data = {
        "名前": ["田中", "佐藤", "鈴木", "高橋", "伊藤"],
        "年齢": [25, 30, 22, 35, 28],
        "部署": ["営業", "開発", "営業", "開発", "人事"],
    }
    return pd.DataFrame(data)


def filter_by_age(df: pd.DataFrame, min_age: int) -> pd.DataFrame:
    """年齢が min_age 以上の人を抽出して返す。"""
    # TODO: df[df["年齢"] >= min_age] を使って実装
    raise NotImplementedError("演習: 年齢フィルタリングを実装してください")


def filter_by_department(df: pd.DataFrame, dept: str) -> pd.DataFrame:
    """指定された部署の人を抽出して返す。"""
    # TODO: df[df["部署"] == dept] を使って実装
    raise NotImplementedError("演習: 部署フィルタリングを実装してください")


def average_age(df: pd.DataFrame) -> float:
    """年齢の平均を返す。"""
    # TODO: df["年齢"].mean() を使って実装
    raise NotImplementedError("演習: 平均年齢の計算を実装してください")


if __name__ == "__main__":
    df = create_employee_df()
    print("=== 社員データ ===")
    print(df)
    print("\n=== 年齢25以上 ===")
    print(filter_by_age(df, 25))
    print("\n=== 開発部 ===")
    print(filter_by_department(df, "開発"))
    print("\n=== 平均年齢 ===")
    print(average_age(df))
