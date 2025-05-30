@echo off
start "" streamlit run C:\Users\Vanessa\Desktop\LEMBRETE_360\LEMBRETE_360.py
timeout /t 5 /nobreak
start "" http://localhost:8501
exit
