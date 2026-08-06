# 【基本】辞書を作って取り出す

# name・age・dept を Key にした辞書を作り、printで表示してみよう
person = {"name": "山田", "age": 25, "dept": "営業部"}
print(person)

# 辞書から name の Value を Keyを指定して printしてみよう
print(person["name"])  # → 山田

# "name" が辞書に存在するか in で確認し、結果を printしてみよう
print("name" in person)  # → True


# 【普通】更新・追加・組み合わせ

# 辞書に新しいKey "hobby" を追加してprintしてみよう
person["hobby"] = "読書"
print(person)

# age の Value を別の数値に更新してprintしてみよう
person["age"] = 26
print(person)

# f文字列を使って「名前: ○○、年齢: △△」と1行で表示してみよう
print(f'名前: {person["name"]}、年齢: {person["age"]}')  # → 名前: 山田、年齢: 26


# 【難しい】複数操作を組み合わせる

# for文とitems()を使って全てのKey・Valueを「Key: Value」の形で表示してみよう
for key, value in person.items():
    print(f"{key}: {value}")

# リストと辞書で同じ情報（name・age・dept）を作り、名前の取り出し方の違いをprintで確認してみよう
person_list = ["山田", 25, "営業部"]
person_dict = {"name": "山田", "age": 25, "dept": "営業部"}
print(person_list[0])       # → 山田（インデックスで指定）
print(person_dict["name"])  # → 山田（Keyで指定）

# "email" が辞書に存在するか確認し、あれば表示・なければ「登録されていません」と表示してみよう
if "email" in person:
    print(person["email"])
else:
    print("登録されていません")