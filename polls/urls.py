from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    # ex: /polls/
    # path('<int:question_id/', views.detail, name='detail'),
    # ex: /polls/5/
    re_path('<int:question_id/', views.detail, name='detail'),
    path('<int:question_id/results/', views.results, name = 'results'),
    # ex: /polls/5/results/
    path('<int:question_id/vote/', views.vote, name='vote'),
    # ex: /polls/5/vote/
]