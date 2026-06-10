input_id = "tanaka"
input_password = "wrong"

correct_id = "tanaka"
correct_password = "pass1234"

if input_id == correct_id and input_password == correct_password:
    print("ログイン成功")
elif input_id == correct_id:
    print("パスワードが違います")
else:
    print("ユーザーが見つかりません")
