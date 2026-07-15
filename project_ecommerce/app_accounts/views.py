from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app_accounts.forms import LoginForm, RegisterForm, VerifyForm
from app_accounts.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app_accounts.utils import generate_verification_code, send_verification_email

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import VerifyForm
from .models import CustomUser

def verify_page(request):
    user_id = request.session.get('verify_user_id')

    if not user_id:
        return redirect('login.page') 

    user = get_object_or_404(CustomUser, id=user_id)
    form = VerifyForm()

    if request.method == "POST":
        form = VerifyForm(request.POST)
        if form.is_valid():
            entered_code = form.cleaned_data['verification_code']

            if entered_code == user.verification_code:
                user.is_verified = True
                user.verification_code = None
                user.save()

                del request.session['verify_user_id']

                return redirect('login.page')
            else:
                form.add_error('verification_code', 'Invalid code')

    return render(request, 'accounts/verify.html', {'form_data': form})

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
                request.session['verify_user_id'] = custom_user.id
                return redirect('verify.page')
            except Exception as e:
                messages.error(request, f'Error sending verification email. Please try again later.')
                return redirect('user.register')
    else:
        form_data = RegisterForm()
    context = {
        'form_data': form_data
    }
    return render(request, 'accounts/register.html', context)

