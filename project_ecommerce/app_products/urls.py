from django.urls import path
from app_products import views

urlpatterns = [
    path('category/create/', views.product_category_create, name='category.create'),
    # for product create and list
    path('create/', views.product_create, name='product.create'),
    path('list/', views.product_index, name='product.index'),
    # for select single product, edit and delete product we need product id and it must be pass via url
    path('view/<int:pk>/', views.product_view, name='product.view'),
    path('edit/<int:pk>/', views.product_edit, name='product.edit'),
    path('delete/<int:pk>/', views.product_delete, name='product.delete'),
    # for product image create and list
    path('image/create/<int:product_id>/', views.product_image_add, name='product_image.create'),
    path('image/edit/<int:product_id>/', views.product_image_add, name='product_image.edit'),
]