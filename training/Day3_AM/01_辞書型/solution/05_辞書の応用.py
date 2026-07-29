# 【基本】

profile = {"name": "山田", "age": 25, "role": "engineer"}
print(profile)
print(f'名前：{profile["name"]}')
print(f'役割：{profile["role"]}')

profile["dept"] = "開発部"
print(profile)


# 【普通】

for key, value in profile.items():
    print(f"{key}：{value}")

settings = {"timeout": 30, "retry": 3, "debug": False}
print(settings["timeout"])
print(settings["retry"])


# 【難しい】

report = {"name": "山田", "score": 85}
report["grade"] = "A"
report["score"] = 90
for key, value in report.items():
    print(f"{key}：{value}")

a = {"code": "A001"}
b = {"code": "B002"}
print(a["code"])
print(b["code"])

print(f'[{profile["name"]}] dept={profile["dept"]} role={profile["role"]}')
