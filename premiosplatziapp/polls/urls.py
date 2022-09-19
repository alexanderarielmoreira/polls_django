from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    #     ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    #    ex: /polls/5/
    #    '<int:question_id>/' -> views based function 
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #    ex: /polls/5/results
    #    '<int:question_id>/results' -> views based function 
    path('<int:pk>/results', views.ResultView.as_view(), name='results'),
    #    ex: /polls/5/votes
    path('<int:question_id>/votes', views.votes, name='votes'),
]


