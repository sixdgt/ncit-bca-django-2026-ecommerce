from django.urls import path
from app_products import views

urlpatterns = [
    path('category/create/', views.product_category_create, name='category.create')
]