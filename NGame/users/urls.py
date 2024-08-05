from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('register_dash/', register_view_dash, name='register_dash'),
    path('logout/', logout_view, name='logout'),
    path("admin", admin_page, name="dashboard_admin"),
    path("client", client_page, name="dashboard_client")
]