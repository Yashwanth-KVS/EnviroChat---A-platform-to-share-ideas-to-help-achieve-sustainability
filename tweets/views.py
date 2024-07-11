from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# tweets/models.py
# tweets/views.py
from django.contrib.auth.models import User
from .models import Tweet


@login_required
def feed(request):
    users = User.objects.all()  # For simplicity, we'll show tweets from all users
    tweets = Tweet.objects.filter(user__in=users).order_by('-created_at')
    return render(request, 'tweets/feed.html', {'tweets': tweets})


def profile(request):
    tweets = Tweet.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tweets/profile.html', {'tweets': tweets})
