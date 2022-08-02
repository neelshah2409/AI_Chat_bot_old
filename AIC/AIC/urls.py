from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('signin',  include("LoginSignup.urls")),
    path('sign',  include("LoginSignup.urls")),
    path('', include("AIC_APP.urls")),
    path('', include("AIC_API.urls")),
]
