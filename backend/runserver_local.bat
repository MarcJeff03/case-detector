@echo off
REM Clear DATABASE_URL and run Django with SQLite
set DATABASE_URL=
REM Add FFmpeg to PATH for audio transcription
set PATH=%PATH%;C:\ProgramData\chocolatey\lib\ffmpeg\tools\ffmpeg\bin
cd /d "%~dp0"
python manage.py runserver
