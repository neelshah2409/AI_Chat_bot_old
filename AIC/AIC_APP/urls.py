from django.urls import path

from . import views

urlpatterns = [
    path('home', views.index, name="Home"),
    path('', views.index, name="Home"),
    path('fetchInputTextArea', views.fetchInputTextArea, name="fetchInputTextArea"),
    path('QueGenerator', views.QueGenerator, name="QueGenerator"),
    path('takeOutputdp', views.takeOutputdp, name="takeOutput")

]
