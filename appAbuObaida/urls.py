from django.urls import path

from appAbuObaida import views

urlpatterns = [
    path('', views.index, name='index'),
    path('questions_blog/', views.questions_blog, name='questions_blog'),
    path('question_detail/<int:pk>/', views.question_detail, name='question_detail'),
    path('events_view/', views.events_view, name='events_view'),
    path('about/', views.about, name='about'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
