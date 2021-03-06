from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from polls.models import Question, Choice

class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'latest_question_list'

  def get_queryset(self):
    #return Question.objects.order_by('-pub_date')[:5]
    return Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
  model = Question
  template_name = 'polls/detail.html'

  def get_queryset(self):
    return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
  model = Question
  template_name = 'polls/results.html'

"""
def index(request):
  # the following was re-written in a convenient shortcut of django:
  #latest_question_list = Question.objects.order_by('-pub_date')[:5]
  #template = loader.get_template('polls/index.html')
  #context = RequestContext(request, {'latest_question_list': latest_question_list, })
  #return HttpResponse(template.render(context))

  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {'latest_question_list': latest_question_list}
  return render(request, 'polls/index.html', context)
"""
"""
def detail(request, question_id):
  # again, re-written with a shortcut-command
  #try:
  #  question = Question.objects.get(pk=question_id)
  #except Question.DoesNotExist:
  #  raise Http404
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/detail.html', {'question': question})
"""

def vote(request, question_id):
  p = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = p.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    return render(request, 'polls/detail.html', {'question': p, 'error_message': "You did not select a choice (or tinkered with the form data)", })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

"""
def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', {'question': question}) """ 
