# 【基本】

point = (10, 20)
lat, lng = point
print(lat)
print(lng)

name, age, city = ("山田", 25, "東京")
print(name)
print(age)
print(city)

print(name + city)


# 【普通】

name, age, city = ("山田", 25, "東京")
print(name + "さんは" + city + "在住で" + str(age) + "歳です")

person = ("山田", 25, "東京")
person_list = list(person)
print(person_list)

person_list = list(person)
person_list[1] = 26
print(person_list)


# 【難しい】

person = ("山田", 25, "東京")
person_list = list(person)
person_list[1] = 26
print(person_list)

a, b, c = (100, 200, 300)
print(a + b + c)

lat, lng = (35.6, 139.7)
print("緯度:" + str(lat) + " 経度:" + str(lng))
