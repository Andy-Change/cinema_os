@echo off
echo [INSTALL] Setting up OS Cinema (Director's Operating System)...

:: 1. Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed. Please install Python 3.10+
    echo Please visit https://python.org
    pause
    exit /b 1
) else (
    for /f "delims=" %%i in ('python --version') do echo [CHECK] %%i detected.
)

:: 2. Check Git
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Git is not installed. Git is required for OS Cinema.
    echo Please install Git for Windows: https://git-scm.com/download/win
    pause
    exit /b 1
) else (
    for /f "delims=" %%i in ('git --version') do echo [CHECK] %%i detected.
)

:: 3. Setup Virtual Environment
if not exist "venv" (
    echo [SETUP] Creating virtual environment...
    python -m venv venv
) else (
    echo [CHECK] Virtual environment found.
)

:: 4. Install/Update Dependencies
echo [SETUP] Updating pip and dependencies...
call venv\Scripts\activate
python -m pip install --upgrade pip >nul 2>&1
if exist "requirements.txt" (
    pip install -r requirements.txt
)

:: 5. System Health Check
echo.
echo [DIAGNOSTICS] Running System Doctor...
python lib/orchestrator.py doctor

echo.
echo [SUCCESS] OS Cinema is ready.
echo Type '/film-init' inside Claude Code to start.
pause
