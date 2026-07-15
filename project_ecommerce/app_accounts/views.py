from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app_accounts.forms import LoginForm, RegisterForm, VerifyForm
from app_accounts.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app_accounts.utils import generate_verification_code, send_verification_email

# Create your views here.
def login_page(request):
    if request.method == "POST":
        request_data = request.POST
        form_data = LoginForm(request_data)
        if form_data.is_valid():
            username = form_data.cleaned_data['username']
            password = form_data.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form_data = LoginForm()
    context = {
        'form_data': form_data
    }
    return render(request, 'accounts/login.html', context)

def register_page(request):
    if request.method == "POST":
        request_data = request.POST
        code = generate_verification_code()
        form_data = RegisterForm(request_data)
        if form_data.is_valid():
            user = form_data.save()
            # for verification code storing to CustomUser model
            custom_user = CustomUser.objects.create(user=
            user, verification_code=code, is_verified=False)
            # verification code will be sent to user email for verification
            try:
                send_verification_email(user.email, code)
                messages.success(request, 'Registration successful. Please check your email for the verification code.')
                return redirect('user.register')
            except Exception as e:
                messages.error(request, f'Error sending verification email. Please try again later.')
                return redirect('user.register')
    else:
        form_data = RegisterForm()
    context = {
        'form_data': form_data
    }
    return render(request, 'accounts/register.html', context)

