# 【基本】

person = {"name": "山田", "status": "active"}
person["status"] = "inactive"
print(person)

person = {"name": "山田"}
person["dept"] = "営業部"
person["age"] = 25
print(person)


# 【普通】

config = {"timeout": 30}
config["retry"] = 3
config["debug"] = True
config["timeout"] = 60
print(config)

if "email" not in config:
    config["email"] = "user@example.com"
print(config)

# print(config["missing"])  # → KeyError


# 【難しい】

data = {"a": 1}
data["b"] = 2
data["a"] = 10
data["c"] = True
print(data)

print(f'name: {data["a"]}, flag: {data["c"]}')

mixed = {"label": "sample", "count": 3, "enabled": True}
print(mixed)
