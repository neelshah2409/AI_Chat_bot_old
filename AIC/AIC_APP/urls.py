from django.urls import path

from . import views

urlpatterns = [
    path('home', views.index, name="Home"),
    path('', views.mainPage, name="mainPage"),
    path('fetchInputTextArea', views.fetchInputTextArea, name="fetchInputTextArea"),
    path('QueGenerator', views.QueGenerator, name="QueGenerator"),
    path('takeOutputdp', views.takeOutputdp, name="takeOutput"),
    path('QueShow', views.QueShow, name="QueShow"),
    path('trainModel', views.trainModel, name="trainModel"),
    path('Showdatafromdb', views.Showdatafromdb, name="Showdatafromdb"),
    path('updateJson', views.updateJson, name="updateJson"),
    path('onlyAnswersData', views.onlyAnswersData, name="onlyAnswersData"),
    path('questionAnswerData', views.questionAnswerData, name="questionAnswerData"),
    # path('getSuggestions', views.getSuggestions, name="getSuggestions"),
    path('linkSubmit', views.linkSubmit, name="linkSubmit"),
    # path('convertCsv', views.convertCsv, name="convertCsv"),
    path('csvSubmit', views.csvSubmit, name="csvSubmit"),
    path('improveFeatures', views.improveFeatures, name="improveFeatures"),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('login', views.Gotoauth, name='Gotoauth'),

]
