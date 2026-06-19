score = 72
age = 22
status = "社員"
favorite = "りんご"
fruits = ["りんご", "バナナ", "みかん"]

if score >= 80:
    print("評価：A")
elif score >= 60:
    print("評価：B")
else:
    print("評価：C")

if age >= 20 and status == "社員":
    print("社員メニュー")

if favorite in fruits:
    print(favorite + "は在庫にあります")
else:
    print(favorite + "は在庫にありません")
