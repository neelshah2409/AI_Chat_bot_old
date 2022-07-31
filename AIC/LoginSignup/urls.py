

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('in', views.signin, name="signin"), #login first page
    path('out', views.signout, name='signout'),
    path('up', views.signup, name='signup'),
    path('', include("AIC_APP.urls"), name='AIC'),

]
