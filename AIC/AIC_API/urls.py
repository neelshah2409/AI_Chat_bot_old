from django.urls import path, include
from .views import ChatAssistantView, ApiKeyView, manageApiKeys

urlpatterns = [
    path('AIC/api/chat_assistant/', ChatAssistantView.as_view(), name="chatAssistantApi"),
    path('AIC/me/api/keys/', ApiKeyView.as_view(), name="apiKeys"),
    path('AIC/me/api/keys/<str:api>', manageApiKeys, name="manageApiKeys"),
    # path('/documentation'),
]
