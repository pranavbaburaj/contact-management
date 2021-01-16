@echo off
cls
python -B contacts/manage.py makemigrations
python -B contacts/manage.py migrate
python -B contacts/manage.py runserver