@echo off

call initialize.bat
call venv\Scripts\activate.bat
python manage.py makemigrations
python manage.py migrate
python populate.py
start http://127.0.0.1:8000/api/v1/schema/swagger-ui/
python manage.py runserver
