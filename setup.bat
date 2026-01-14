@echo off
echo [INSTALL] Setting up Director's Operating System...

:: 1. Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed. Please install Python 3.10+
    pause
    exit /b 1
)

:: 2. Setup Virtual Environment
if not exist "venv" (
    echo [SETUP] Creating virtual environment...
    python -m venv venv
)

:: 3. Install Dependencies (if reqs exist)
if exist "requirements.txt" (
    echo [SETUP] Installing dependencies...
    call venv\Scripts\activate
    pip install -r requirements.txt
)

:: 4. Initial Status Check
echo [SUCCESS] System ready.
echo.
python lib/orchestrator.py status
pause
