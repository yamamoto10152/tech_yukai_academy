password = ""
count = 0

while password != "2027":
    password = input("Pass?")
    if password != "2027":
        count += 1
        print(f"残り {3 - count} 回です")
        if count >= 3:
            print("強制終了します")
            break

if password == "2027":
    print("ログイン成功！")
