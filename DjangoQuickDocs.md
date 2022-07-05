## Django Quick Docs Overview:
This Docs is a personalised jump start documentation for django app.

### Install and runserver:
 
 - Setup venv virtualizatio env: From inside Directory "python -m venv .venv" to setup venv. A common directory location for a virtual environment is .venv
  - Activate venv and install Django: Activate by "Scripts\activate.bat" and install Django inside the vend by "py -m pip install Django"

  - Store the venv installed packages by running "pip freez" in requirments.txt to re-setup venv exactly same by "pip install -r requirments.txt"

  - Create Project: by running "django-admin startproject projectname"
  - cd into the project then run "python manage.py runserver" or "python manage.py runserver 7000"

### Django Project and Apps:
  - Project is the overall website
  - Apps can be multiple within a project like blog, shop, poll, pages etc. 


### Django Initial/Core Files in Project Directory:
  - manage.py : Commandline tool for Django, used to create migrations, run the server, etc.
  - _init_.py : 
  - settings.py : Config/Settings file for Base Directory, Secret Key for production, Installed Apps, Middlewares, Templates, Database, etc.
  - urls.py : its our Route file.
  - wsgi.py : Django’s primary deployment platform is WSGI, the Python standard for web servers and applications. Django’s startproject management command sets up a minimal default WSGI configuration for you, which you can tweak as needed for your project, and direct any WSGI-compliant application server to use.

### Default Migrations:
"python manage.py migrate"

### Creating App and initial Directory Structure:
"python manage.py startapp appname"
this will create a new folder inside our project. inside the newly createdapp
  - migrations/ : this folder is for listing migrations
  - admin.py : for adding somethig to the admin area
  - apps.py : app's config file
  - models.py : for creating database models/tables and or relationships
  - tests.py : test codes
  - views.py : for rendering serverside template or REST APIs

### Routes and urls.py | project level and app level:
Its good practice to add a urls.py routes file for every apps inside aproject and include that url file inside project's urls.py
```py
# Project level urls.py
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]


# App level urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
  
### Views:
```py
from django.http import HttpResponse

# this index method will be called from app level's urls.py route file
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

### Creating/Adding Models:
models.py inside app level holds the database structure/table for that app
```py
from django.db import models

# Create your models here.
class Question(models.Model):
    # id field will be created automatically
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text =  models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
```
