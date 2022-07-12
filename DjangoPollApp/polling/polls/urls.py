from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # ex: /polls/7/
    path('<int:question_id>', views.detail, name='details'),
    # ex: /polls/results/7
    path('<int:question_id>/results', views.result),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
