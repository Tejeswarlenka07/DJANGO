from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('hi/',views.hi),
    path('bye',views.bye),
    path('', views.home, name='home'),
    

]
