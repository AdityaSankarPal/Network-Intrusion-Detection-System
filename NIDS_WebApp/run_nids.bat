@echo off
title AI Network Intrusion Detection System 
echo ========================================================
echo   STARTING AI NETWORK INTRUSION DETECTION SYSTEM
echo ========================================================
echo.
echo Installing/Verifying dependencies...
pip install -r requirements.txt
echo.
echo Launching Streamlit Cyber Dashboard...
streamlit run app.py
pause