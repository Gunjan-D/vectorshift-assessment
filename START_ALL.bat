@echo off
echo ========================================
echo VectorShift Project - Starting Services
echo ========================================
echo.

REM Set PATH for portable tools
set PATH=C:\Users\gdeshpande\portable_tools\node-v20.18.1-win-x64;C:\Users\gdeshpande\portable_tools\redis;%PATH%

REM Check Redis
echo Checking Redis...
C:\Users\gdeshpande\portable_tools\redis\redis-cli.exe ping >nul 2>&1
if %errorlevel% neq 0 (
    echo Starting Redis...
    start "Redis Server" C:\Users\gdeshpande\portable_tools\redis\redis-server.exe
    timeout /t 2 >nul
) else (
    echo Redis is already running!
)

REM Start Backend
echo Starting Backend Server...
start "Backend - Port 8000" cmd /k "cd /d C:\Users\gdeshpande\Downloads\automations_technical_assessment\integrations_technical_assessment\backend && python -m uvicorn main:app --reload"

REM Wait a bit
timeout /t 3 >nul

REM Start Frontend
echo Starting Frontend Server...
start "Frontend - Port 3000" cmd /k "cd /d C:\Users\gdeshpande\Downloads\automations_technical_assessment\integrations_technical_assessment\frontend && npm start"

echo.
echo ========================================
echo Services Starting...
echo ========================================
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
echo.
echo Press any key to exit this window...
pause >nul
