

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signin, name="signin"), #login first page
    path('signout', views.signout, name='signout'),
    path('signup', views.signup, name='signup'),
    path('', include("AIC_APP.urls"), name='AIC'),



]
