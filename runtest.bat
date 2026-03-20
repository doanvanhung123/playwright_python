@echo off

set BROWSER=%1
set WORKERS=%2
set ENV=%3
set MARKER=%4

if "%BROWSER%"=="" set BROWSER=chromium
if "%WORKERS%"=="" set WORKERS=2
if "%ENV%"=="" set ENV=dev

set TEST_ENV=%ENV%

echo ===== RUN CONFIG =====
echo Browser: %BROWSER%
echo Workers: %WORKERS%
echo Env: %ENV%
echo Marker: %MARKER%

if "%MARKER%"=="" (
    python -m pytest -n %WORKERS% --alluredir=allure-results
) else (
    python -m pytest -n %WORKERS% -m "%MARKER%" --alluredir=allure-results
)