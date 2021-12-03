from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from polls.models import Question, AnswerList

# Create your views here.
def index(request):
	lastest_question_list = Question.objects.all().order_by('-pub_date')[:5]
	context = {'lastest_question_list': lastest_question_list}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	context = {'question': question}
	return render(request, 'polls/detail.html', context)

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selection_obj = question.answerlist_set.get(pk=request.POST['choice'])
	except (KeyError, AnswerList.DoesNotExist):
		context = {'question': question, 'error_msg':"You didn't select"}
		return render(request, 'polls/detail.html', context)
	else:
		selection_obj.votes += 1
		selection_obj.save()
		return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))


def result(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	context = {'question' : question}
	return render(request, 'polls/result.html', context)