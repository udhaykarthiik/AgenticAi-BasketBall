# dashboard/urls.py

from django.urls import path
from . import views

# The 'app_name' line has been removed to fix the error.

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
]