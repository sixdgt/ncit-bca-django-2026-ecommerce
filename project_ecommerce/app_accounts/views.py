from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from app_accounts.forms import LoginForm, RegisterForm, VerifyForm
from app_accounts.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app_accounts.utils import generate_verification_code, send_verification_email
from app_orders.models import Order
from .forms import VerifyForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required

# Create your views here.  
@login_required
def profile_view(request):
    user = request.user

    # All orders (latest first)
    orders = Order.objects.filter(user=user).order_by('-created_at')

    # Latest order
    latest_order = orders.first()

    return render(request, 'accounts/profile.html', {
        'user': user,
        'orders': orders,
        'latest_order': latest_order
    })

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login.page')

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
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                custom_user = CustomUser.objects.filter(user=user)
                if custom_user.exists() and custom_user.first().is_verified:
                    login(request, user)
                    request.session['verify_user_id'] = user.id
                    messages.success(request, 'Login successful.')
                    return redirect('profile')
                else:
                    messages.error(request, 'Your account is not verified. Please check your email for the verification code.')
                    request.session['verify_user_id'] = user.id
                    return redirect('verify.page')
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('login.page')
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
            return redirect('login.page')
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
            custom_user = CustomUser.objects.create(user=user, verification_code=code, is_verified=False)
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

