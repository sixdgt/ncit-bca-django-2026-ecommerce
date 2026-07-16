from django.urls import path
from app_orders import views

urlpatterns = [
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('checkout/', views.checkout_page, name='checkout.page')
]