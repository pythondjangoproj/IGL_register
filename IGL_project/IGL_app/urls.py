from django.urls import path, include
from .views import UserRegisterApi

app_name = 'IGL_app'

urlpatterns = [
    path('api/user_register', UserRegisterApi.as_view()),
]