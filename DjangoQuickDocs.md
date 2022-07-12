## Django Quick Docs Overview:
This Docs is a personalised jump start documentation for django app.

### Architecture:
Django is an MVT (Model, View, Template) based framework. Where View acts like "Controller" in MVC.

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
  - views.py : It's the controller, for rendering serverside template or REST APIs

### Routes and urls.py | project level and app level:
Its good practice to add a urls.py routes file for every apps inside aproject and include that url file inside project's urls.py
Docs : https://docs.djangoproject.com/en/4.0/topics/http/urls/
Uses: https://docs.djangoproject.com/en/4.0/intro/tutorial03/
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
Views acts like controller (MVC). Note Django uses MVT (Model, View, Template)
```py
from django.http import HttpResponse

# this index method will be called from app level's urls.py route file
# https://docs.djangoproject.com/en/4.0/ref/request-response/ for request object
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    # All Django wants is that HttpResponse Or raising an exception
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

### Layout Extending and index view in Template Directory:
```html
<!-- layout.html or base.html -->
<html>
    <body>
        <div class="col-md-6 m-auto">
            {% block content %}{% endblock content %}
        </div>
    </body>
</html>

<!-- index.html -->
{% extends 'base.html' %} {% block content %}
<h1 class="text-center mb-3">Polls Questions</h1>
{% if latest_question_list %} {% for question in latest_question_list %}
<p class="lead">{{ question.question_text }}</p>
<a href="{% url 'polls:details' question.id %}">Vote Now</a>
{% comment %} polls:details will mathch with urls name defiened in urls.py urlpatterns {% endcomment %}
<a href="/polls/results/{{question.id}}">Show Results</a>
{% comment %} Can also be defiened like this {% endcomment %}
{% endfor %} {% else %}
<p class="">No Polls</p>
{% endif %} {% endblock %}
```

### Dynamic Links With UrlParams, Receiving Params in urls.py (Route):
```html

<!-- Dynamic Links With UrlParams -->
<!-- {% url %} template tag help easily change URLs on projects with a lot of templates if name argument is defined in the path() inside urls.py -->
<a href="{% url 'polls:detail' question.id %}" class="btn btn-primary btn-sm">Vote Now</a>

<!-- We can also use hard urls, but it is hard if we change url structure in future inside urls.py -->
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
<!-- {% comment %} Can also be defiened like this, but url template tag is conveinent {% endcomment %} -->

<!-- # the 'name' value as called by the {% url %} template tag
path('<int:question_id>/', views.detail, name='detail'), -->
```
```py
# urls.py
path('<int:question_id>', views.detail, name='detail')
# <int:question_id>. Using angle brackets “captures” part of the URL and sends it as a keyword argument to the view function. The question_id part of the string defines the name that will be used to identify the matched pattern, and the int part is a converter that determines what patterns should match this part of the URL path. The colon (:) separates the converter and pattern name.

# views.py
# Show single question and choices
def detail(request, question_id):
    print_arguments(request)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question Doesn\'t Found')
    return render(request, 'polls/results.html', { 'question': question })
```

### render() shortcut:
load a template, fill a context (dictionary) and return an HttpResponse object with the result of the rendered template. Django provides a shortcut
```py
# without using render(), we have to use loader.getTemplate(....) and return HttpResponse also importing them
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

# Using render(), we no longer need to import loader and HttpResponse (you’ll want to keep HttpResponse if you still have the stub methods for detail, results, and vote)
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```