from django.urls import path
from app_accounts import views

urlpatterns = [
    path('login/', views.login_page, name='login.page'),
    path('register/', views.register_page, name='user.register'),
    path('verify/', views.verify_page, name='verify.page'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout')
]