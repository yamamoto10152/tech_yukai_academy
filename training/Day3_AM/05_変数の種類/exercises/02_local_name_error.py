"""
演習1-B: ローカル変数は外から見えない
show_info() のあとに print(dept) を追加して実行し、
NameError になることを確認してください。

ヒント:
- dept は関数の中だけのローカル変数
- エラーメッセージと PDF を照らし合わせる
"""


def show_info():
    dept = "技術部"


show_info()

# TODO: ここに print(dept) を書いて実行する
