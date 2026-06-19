from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

with open(DATA / "settings.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

settings = {}
for line in lines:
    key, value = line.strip().split("=")
    settings[key] = value

print("theme:", settings["theme"])
print("language:", settings["language"])
print("max_users:", settings["max_users"])
