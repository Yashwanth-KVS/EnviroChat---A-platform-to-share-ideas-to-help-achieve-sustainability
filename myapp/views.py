from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetConfirmView, LoginView, PasswordResetView

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
            return redirect('myapp:dashboard')
    else:
        logger.debug("GET request received in register view")
        form = UserRegisterForm()
    return render(request, 'myapp/register.html', {'form': form})

def user_login(request):
    logger.debug("Login view called")
    if request.method == 'POST':
        logger.debug("POST request received in login view")
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            logger.debug("Form is valid in login view")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                logger.debug(f"User {username} logged in successfully")
                return redirect('myapp:register')
            else:
                messages.error(request, 'Invalid username or password')
                logger.debug(f"Invalid login attempt for username: {username}")
    else:
        logger.debug("GET request received in login view")
        form = UserLoginForm()
    return render(request, 'myapp/login.html', {'form': form})

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'myapp/password_reset_confirm.html'
    success_url = reverse_lazy('myapp:login')

    def form_valid(self, form):
        messages.success(self.request, 'Your password was successfully changed.')
        return super().form_valid(form)

class CustomPasswordResetView(PasswordResetView):
    template_name = 'myapp/password_reset.html'
    email_template_name = 'myapp/password_reset_email.html'
    subject_template_name = 'myapp/password_reset_subject.txt'
    success_url = reverse_lazy('myapp:password_reset_done')
    success_message = "Password reset link has been sent to your email."


def dashboard(request):
    return render(request, 'myapp/dashboard.html')

def user_logout(request):
    if request.method == "POST":
        auth_logout(request)
        messages.add_message(
            request,
            messages.SUCCESS,
            "You have successfully logged out !!",
            extra_tags="success",
        )
        return redirect("myapp:login")
    return redirect("myapp:dashboard")