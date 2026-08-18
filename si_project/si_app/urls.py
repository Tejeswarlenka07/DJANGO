from django.urls import path
from . import views

urlpatterns = [
    path('', views.simple_interest, name='simple_interest'),
]
