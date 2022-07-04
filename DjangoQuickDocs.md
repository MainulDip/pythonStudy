## Django Quick Docs Overview:
This Docs is a personalised jump start documentation for django app.

### Install and runserver:
 
 - Setup venv virtualizatio env: From inside Directory "python -m venv .venv" to setup venv. A common directory location for a virtual environment is .venv
  - Activate venv and install Django: Activate by "Scripts\activate.bat" and install Django inside the vend by "py -m pip install Django"

  - Store the venv installed packages by running "pip freez" in requirments.txt to re-setup venv exactly same by "pip install -r requirments.txt"

  - Create Project: by running "django-admin startproject projectname"
  - cd into the project then run "python manage.py runserver"