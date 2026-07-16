from django.urls import path
from app_carts import views

urlpatterns = [
    path('view/', views.cart_page, name='cart.page'),
    path('wishlist/', views.wishlist_page, name='wishlist.page'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add.cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove.from.cart'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add.to.wishlist'),
    path('remove-from-wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove.from.wishlist'),
    path('update-cart-item/<int:product_id>/', views.update_cart_item, name='update.cart.item'),
]