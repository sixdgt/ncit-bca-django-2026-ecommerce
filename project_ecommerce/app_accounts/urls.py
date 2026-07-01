from django.urls import path
from app_accounts import views

urlpatterns = [
    path('login/', views.login_page, name='login.page'),
]