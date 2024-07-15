from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.forms import PasswordResetForm

import logging

logger = logging.getLogger(__name__)

def register(request):
    logger.debug("Register view called")
    if request.method == 'POST':
        logger.debug("POST request received in register view")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            logger.debug("Form is valid in register view")
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            logger.debug(f"Account created for {username}")
            return redirect('myapp:login')
    else:
        logger.debug("GET request received in register view")
        form = UserRegisterForm()
    return render(request, 'myapp/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('myapp:dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'myapp/login.html')

def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                use_https=request.is_secure(),
                email_template_name='myapp/password_reset_email.html',
                subject_template_name='myapp/password_reset_subject.txt'
            )
            messages.success(request, 'Password reset link has been sent to your email.')
            return redirect('myapp:login')
    else:
        form = PasswordResetForm()
    return render(request, 'myapp/password_reset.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'myapp/dashboard.html')
