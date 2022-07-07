from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Choice

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# Get Questions and Dispay
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)