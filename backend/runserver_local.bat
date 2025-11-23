@echo off
REM Clear DATABASE_URL and run Django with SQLite
set DATABASE_URL=
cd /d "%~dp0"
python manage.py runserver
