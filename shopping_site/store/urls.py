from django.urls import path
from . import views

urlpatterns = [
    path('product1/', views.product1),
    path('product2/', views.product2),
    path('product3/', views.product3),
    path('cart/', views.cart_view),
]
