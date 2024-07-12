from django.shortcuts import render
from .models import Followers
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, '')


# Create your views here.
def followers(request, latest_tweets=None):
    follow_request = followers.objects.filter(STATUS_CHOICES=1)
    context = {'latest_tweets': latest_tweets}
    return render(request, 'myapp/templates/myapp/tweet.html', context)


def search_members(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        query = request.GET.get('query', '')
        members = Member.objects.filter(first_name__icontains=query)
        results = [{'id': member.id, 'name': member.first_name} for member in members]
        return JsonResponse(results, safe=False)
    return render(request, 'search.html')
