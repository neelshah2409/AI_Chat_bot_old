
from . import views
from django.urls import path, include


urlpatterns = [

    path('', views.index, name="AIC"),
    path('fetchInputTextArea', views.fetchInputTextArea, name="fetchInputTextArea"),
    path('QueGenerator', views.QueGenerator, name="QueGenerator"),
    path('howToUse', views.generateFAQs, name="generateFAQs"),
    path('takeOutputdp', views.takeOutputdp, name="takeOutput"),
    path('QueShow', views.QueShow, name="QueShow"),
    path('trainModel', views.trainModel, name="trainModel"),
    path('chatAssistant', views.chatAssistant, name="chatAssistant"),
    # path('Showdatafromdb', views.Showdatafromdb, name="Showdatafromdb"),
    path('updateJson', views.updateJson, name="updateJson"),
    path('onlyAnswersData', views.onlyAnswersData, name="onlyAnswersData"),
    path('questionAnswerData', views.questionAnswerData, name="questionAnswerData"),
    path('linkSubmit', views.linkSubmit, name="linkSubmit"),
    path('fileSubmit', views.fileSubmit, name="csvSubmit"),
    path('improveFeatures', views.improveFeatures, name="improveFeatures"),
    path('questionAnswers', views.questionAnswers, name="questionAnswers"),
    path('onlyAnswers', views.onlyAnswers, name="onlyAnswers"),
    path('linkInput', views.linkInput, name="linkInput"),
    path('filesInput', views.filesInput, name="filesInput"),
    path('paragraph', views.paragraph, name="paragraph"),
    path('resetAll', views.resetAll, name="resetAll"),
    path('getIntentsData', views.getIntentsData, name="getIntentsData"),
    path('getUserData', views.getUserData, name="getUserData"),
    path('updateUserData', views.updateUserData, name="updateUserData"),

    path('api', views.api, name="api"),
        path('translate', views.translate, name="translate")

    # path('signup', views.signup, name='signup'),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    # path('signin', views.signin, name='signin'), #login sign in page
    # path('signout', views.signout, name='signout'),#login sign out page
    # path('login', views.Gotoauth, name='Gotoauth'), #login authentication page
    # path('', include("LoginSignup.urls")),

]
