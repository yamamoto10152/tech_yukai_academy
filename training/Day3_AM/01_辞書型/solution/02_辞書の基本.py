# 【基本】

person = {"name": "山田", "age": 25, "dept": "営業部"}
print(person)
print(person["name"])

empty = {}
print(empty)


# 【普通】

scores = {"math": 80, "english": 95, "science": 72}
print(scores["math"])
print(person["age"])
print(person["dept"])
print("name" in person)


# 【難しい】

print(f'名前: {person["name"]}、年齢: {person["age"]}')

as_list = ["山田", 25, "営業部"]
print(as_list[0])
print(person["name"])

print(person["name"])
print(person["age"])
print(person["dept"])
