from django.urls import path
from app_ecomweb import views

urlpatterns = [
    path('', views.landing_page, name='landing.page'),
    path('about/', views.about_page, name='about.page'),
    path('faq/', views.faq_page, name='faq.page'),
    path('cart/', views.cart_page, name='cart.page'),
    path('wishlist/', views.wishlist_page, name='wishlist.page'),
    path('checkout/', views.checkout_page, name='checkout.page'),
]