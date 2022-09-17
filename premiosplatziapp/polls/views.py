from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


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
    return HttpResponse(f'<h1>Estas votando a la pregunta N° {question_id}</h1>')

