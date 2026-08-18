from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_user, name='add'),
    path('save/', views.save_user, name='save'),
    path('view/', views.view_users, name='view'),
    path('edit/<int:id>/', views.edit_user, name='edit'),
    path('update/<int:id>/', views.update_user, name='update'),
    path('delete/<int:id>/', views.delete_user, name='delete'),
]