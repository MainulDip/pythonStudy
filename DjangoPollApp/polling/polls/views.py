from ast import Try
from cgi import print_arguments
from pprint import PrettyPrinter
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Choice

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# Get Questions and Dispay
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Show single question and choices
def detail(request, question_id):
    print(request.method, 'cool')
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question Doesn\'t Found')
    # return render(request, 'polls/results.html', { 'question': question })
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    return render(request, 'polls/detail.html', {'question': question})



# Show Voting Results
def result(request, question_id):
    # response = "Voting result is %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# Allow to vote
def vote(request, question_id):
    # response = "Voting result is %s."
    # return HttpResponse(response % question_id)
    print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't vote yet",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        # return HttpResponseRedirect('polls:results', question_id, question=question)
