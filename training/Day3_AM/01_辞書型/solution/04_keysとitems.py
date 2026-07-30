# 【基本】

person = {"name": "山田", "age": 25, "dept": "営業部"}
print(person.keys())
print(person.values())
print(person.items())


# 【普通】

for key, value in person.items():
    print(key, value)

for key, value in person.items():
    print(f"{key}: {value}")

print(len(person))


# 【難しい】

profile = {"name": "山田", "age": 25, "dept": "営業部", "role": "engineer"}
for key, value in profile.items():
    print(f"{key}：{value}")

print(list(person.keys()))

dict_a = {"a": 1, "b": 2}
dict_b = {"x": 10, "y": 20}
for key, value in dict_a.items():
    print(key, value)
for key, value in dict_b.items():
    print(key, value)
