from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse 


def index(request):
    latest_question_list = Question.objects.all() #esto trae un objeto de tipo 'queryset' 
    return render(request, 'polls/index.html', {
    #          key            :        value
        'latest_question_list': latest_question_list
    })    
 

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {
        'question':question
    }) 


def results(request, question_id):
    return HttpResponse(f'<h1>Estas viendo los resultados de la pregunta N° {question_id}</h1>')


def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message': 'No ha seleccionado una respuesta.' 
        })
    else:
        selected_choice.votes += 1 
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

