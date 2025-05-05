#!/bin/bash

source initialize.sh
source venv/bin/activate
python manage.py makemigrations
python manage.py migrate
python populate.py
python manage.py runserver
