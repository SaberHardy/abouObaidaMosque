from django.urls import path

from appAbuObaida import views

urlpatterns = [
    path('', views.index, name='index'),
]
