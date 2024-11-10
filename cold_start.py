import os
from pathlib import Path

from apps.base.sys import (
    is_linux,
    is_mac,
    is_windows,
)
from core.settings import LOCAL_APPS
from core.settings import DATABASES

APPS_MIGRATIONS_PATH = [f"apps/{app}/migrations" for app in LOCAL_APPS]

if DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3':
    if is_windows():
        os.system("del db.sqlite3")
        print("Deleted db.sqlite3")
    elif is_linux() or is_mac():
        os.system("rm db.sqlite3")

elif DATABASES['default']['ENGINE'] == 'django.db.backends.postgresql':
    if is_windows():
        os.system('psql -U admin -c "DROP DATABASE IF EXISTS ims;"')
        os.system('psql -U admin -c "CREATE DATABASE ims;"')
    elif is_mac() or is_linux():
        os.system("PGPASSWORD=github.com dropdb -p 5432 -h 127.0.0.1 -e ims -U admin")
        os.system("PGPASSWORD=github.com createdb -p 5432 -h 127.0.0.1 -e ims -U admin")

for path in APPS_MIGRATIONS_PATH:
    directory = Path(path)
    try:
        for file in directory.iterdir():
            if file.is_file():
                file.unlink()
    except FileNotFoundError:
        pass

APPS_LIST_STR = " ".join(LOCAL_APPS)

os.system(f"python manage.py makemigrations {APPS_LIST_STR}")
os.system("python manage.py migrate")
os.system("python manage.py runscript seed")
os.system("python manage.py runserver")
