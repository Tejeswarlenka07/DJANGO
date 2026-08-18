from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('register/', views.register_form, name='register'),
    path('register-result/', views.register_result, name='register_result'),
]