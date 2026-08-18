from django.urls import path
from . import views

urlpatterns = [
    path('hello1/', views.hello),
]
