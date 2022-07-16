from django.urls import path
from . import views

urlpatterns = [
    # / homemage
    path('', views.index, name='index'),
]