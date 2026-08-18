from django.urls import path
from .views import EmployeeListCreate, EmployeeRetrieveUpdateDelete

urlpatterns = [
    path('', EmployeeListCreate.as_view()),   # root
    path('<int:pk>/', EmployeeRetrieveUpdateDelete.as_view()),
]
