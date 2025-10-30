@echo off
echo Setting up environment...
python -m venv venv
call venv\Scripts\activate
pip install flask matplotlib
flask --app app run
pause
