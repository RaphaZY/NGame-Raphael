from django.urls import path
from .views import *

urlpatterns = [
    path('', dash, name='dash'),
    path('users', dash_users, name='dash_users'),
   
]