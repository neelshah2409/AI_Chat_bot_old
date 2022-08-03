"""AIC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from AIC_API.views import ChatAssistantView, ApiKeyView, manageApiKeys

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign',  include("LoginSignup.urls")),
    path('', include("AIC_APP.urls")),
    path('AIC/api/chat_assistant/', ChatAssistantView.as_view(), name="chatAssistantApi"),
    path('AIC/me/api/keys/', ApiKeyView.as_view(), name="apiKeys"),
    path('AIC/me/api/keys/<str:api>', manageApiKeys, name="manageApiKeys"),
]
