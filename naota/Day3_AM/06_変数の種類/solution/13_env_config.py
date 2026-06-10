import os

APP_LANG = os.environ.get("APP_LANG", "ja")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DEBUG_MODE = os.environ.get("DEBUG_MODE", "false")

print("APP_LANG:", APP_LANG)
print("DB_HOST:", DB_HOST)
print("DEBUG_MODE:", DEBUG_MODE)
