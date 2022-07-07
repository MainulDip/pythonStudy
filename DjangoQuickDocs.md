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
Then need to add app level's apps.py class inside the project's settings.py's installed apps list/array. 
```py
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    .......
]
```

This will tell the projects command line tool to look inside of the app's (polls) directory to generate command on that context.

Now to run the migration from project's directory run this
```sh
python manage.py makemigrations polls
# This will create a new migration file inside app levels migration directory (polls\migrations\0001_initial.py)

python .\manage.py migrate
# This will commit migration
```

### Model interactive shell:
```sh
python manage.py shell
# This will open interactive shell to play with database as model defined
from polls.models import Question, Choice
from django.utils import timezone

# questions list
Question.objects.all()
# adding Question
q = Question(question_text = 'What is your favourite Python Framework?', pub_date=timezone.now())
# saving into satabase
q.save()
# return id and text
q.id
q.question_text()

#getting question lists
Question.objects.filter(id=1) # return array/list
Question.objects.get(pk=1) # return single item

# show all the options of the question
q.choice_set.all()

# add some options to the questions for voting
q.choice_set.create(choice_text="Django", votes=0)
q.choice_set.create(choice_text="Flask", votes=0)
q.choice_set.create(choice_text="Web2py", votes=0)

# show all the options of the question
q.choice_set.all()
```

### Creating Superuser Admin:
Out-of-the-box django provide some defaul functionality like manage users, create super user, etc.
```sh
python manage.py createsuperuser
# this will ask for input name and password to create the superuser
```

### Adding Admin Functionality For Apps:
App level's admin.py is used to provide admin functionalities
Look official walkthrough for more details at : https://docs.djangoproject.com/en/4.0/intro/tutorial07/

```py
from django.contrib import admin
from .models import Question, Choice

# Register your models here.

# admin.site.register([Question, Choice])
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline): # admin.StackedInline for vertical listing
    model = Choice
    extra = 0 # how many extra row after lisitng all options
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
``` 

### Admin area site info:
```py
# inside app's admin.py
admin.site.site_header = "Polls Admin Header"
admin.site.site_title = "title Polls"
admin.site.index_title = "Welocome Admin From index_title"
```

### Adding Template Directory:
To keep all the template files in an organised place, place the templates folder in projects directory and customise the settings.py's template config to point out the Template directory. Also place template files separate by app's name.
Docs: https://docs.djangoproject.com/en/4.0/intro/tutorial07/