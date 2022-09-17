from django.urls import path
from . import views

urlpatterns = [
    #ex: /polls/
    path('', views.index, name='index'),
    #ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detalle'),
    #ex: /polls/5/results
    path('<int:question_id>/results', views.results, name='resultados'),
    #ex: /polls/5/votes
    path('<int:question_id>/votes', views.votes, name='votos'),
]


