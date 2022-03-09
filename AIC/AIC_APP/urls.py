from django.urls import path

from . import views

urlpatterns = [
    path('home', views.index, name="Home"),
    path('', views.index, name="Home"),
    path('takeOutput', views.takeOutput, name="takeOutput"),

]
