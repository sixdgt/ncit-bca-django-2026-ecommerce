from django.urls import path
from app_ecomweb import views

urlpatterns = [
    path('', views.landing_page, name='landing.page'),
    path('about/', views.about_page, name='about.page'),
    path('faq/', views.faq_page, name='faq.page'),
]