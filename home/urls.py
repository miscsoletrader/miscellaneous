from django.urls import path
from . import views  # to get created view from views.py

""" URL for home.html & contact.html """
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact')
]
