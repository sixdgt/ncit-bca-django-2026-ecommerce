from django.urls import path
from app_ecomweb import views

urlpatterns = [
    path('', views.landing_page, name='landing.page'),
    path('about/', views.about_page, name='about.page'),
    path('faq/', views.faq_page, name='faq.page'),
    path('product/<slug:slug>/<int:product_id>/', views.product_detail, name='product.detail'),
]