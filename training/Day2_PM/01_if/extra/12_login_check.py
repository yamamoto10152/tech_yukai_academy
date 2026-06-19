"""
チャレンジアップ 02: ログイン判定（and / == の応用）
正しいユーザーIDとパスワードの組み合わせだけ「ログイン成功」と表示してください。
それ以外は、状況に応じて次のメッセージを出し分けてください。

- IDもパスワードも正しい     → 「ログイン成功」
- IDは正しいがパスワードが違う → 「パスワードが違います」
- IDが登録されていない        → 「ユーザーが見つかりません」

正解: user_id = "tanaka", password = "pass1234"

ヒント: まず ID が正しいかを判定し、その中でパスワードを and で確認する
"""

input_id = "tanaka"
input_password = "wrong"

correct_id = "tanaka"
correct_password = "pass1234"

# TODO: if / elif / else で3パターンに分岐する

