@echo off
echo HYPERBOLIC FUNHOUSE MIRRORS
echo ============================
echo.
echo 1. Installing dependencies...
pip install -r requirements.txt

echo.
echo 2. Running the model...
python -m src.main

echo.
echo 3. Opening results...
if exist figures\results.png start figures\results.png

echo.
echo 4. Checking data...
if exist data\parameters.txt type data\parameters.txt

echo.
pause
