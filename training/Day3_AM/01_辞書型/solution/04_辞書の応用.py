"""
Day3: 辞書の応用（教材参考）
実行: python training/day03/辞書型/solution/04_辞書の応用.py
"""

profile = {
    "name": "山田",
    "age": 25,
    "role": "engineer",
}

print(f'名前：{profile["name"]}')   # → 名前：山田
print(f'役割：{profile["role"]}')    # → 役割：engineer

profile["dept"] = "開発部"
print(profile)   # → {'name': '山田', 'age': 25, 'role': 'engineer', 'dept': '開発部'}

for key, value in profile.items():
    print(f"{key}：{value}")
