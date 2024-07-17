from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
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

@login_required
def dashboard(request):
    return render(request, 'myapp/dashboard.html')
