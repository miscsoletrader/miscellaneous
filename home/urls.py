from django.urls import path
from . import views  # to get created view from views.py

urlpatterns = [
    path('', views.home, name='home'),
]
