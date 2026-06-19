age = 25
status = "社員"
score = 100
is_leader = False
is_raining = False

if age >= 20 and status == "社員":
    print("社員向けの処理を実行")

if score == 100 or is_leader:
    print("特別扱い")

if not is_raining:
    print("傘は不要です")
