from django.urls import path

from appAbuObaida import views

urlpatterns = [
    path('', views.index, name='index'),
    path('questions_blog/', views.questions_blog, name='questions_blog'),
    path('question_detail/', views.question_detail, name='question_detail'),
]
