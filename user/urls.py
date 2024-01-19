from django.urls import path, include
from .views import user_registration, user_login

urlpatterns = [
    path('registration/', user_registration, name='user_registration'),
    path('login/', user_login, name='user_login'),
]
