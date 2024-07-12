from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Followers, Member
from .forms import FollowerForm
from django.http import JsonResponse

    return render(request, 'register.html', {'form': form})

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
# Create your views here.
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
def followers_view(request):
    # Check if there are any followers in the database

    show_requests = request.GET.get('show_requests') == 'on'

    # Static list of followers for display (this is separate from the form)
    static_followers = [
        {'follower': 'John', 'followee': 'Jack', 'status': 1},
        {'follower': 'Jack', 'followee': 'Charles', 'status': 1},
        {'follower': 'Charles', 'followee': 'David', 'status': 1},
        {'follower': 'David', 'followee': 'Alex', 'status': 1},
        {'follower': 'Alex', 'followee': 'John', 'status': 1},
    ]

    if request.method == 'POST':
        form = FollowerForm(request.POST)
        if form.is_valid():
            # Handle form submission if needed
            # You can convert the chosen names back to the actual member instances if necessary
            return redirect('followers')  # Redirect to the same view to see the new entry
    else:
        form = FollowerForm()

    # Always return a rendered response
    return render(request, 'followers.html',
                  {'followers': static_followers, 'show_requests': show_requests, 'form': form})


def search_members(request):
    static_followers = [
        {'follower': 'John', 'followee': 'Jack', 'status': 1},
        {'follower': 'Jack', 'followee': 'Charles', 'status': 1},
        {'follower': 'Charles', 'followee': 'David', 'status': 1},
        {'follower': 'David', 'followee': 'Alex', 'status': 1},
        {'follower': 'Alex', 'followee': 'John', 'status': 1},
    ]
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        query = request.GET.get('query', '')
        members = Member.objects.all()
        print(members)
        members = Member.objects.filter(first_name__icontains=query)
        # results = [{'id': member.id, 'name': member.first_name} for member in members]
        results = [
        {'id': 'John', 'name': 'Jack'},
        {'id': 'Jack', 'name': 'Charles'},
        {'id': 'Charles', 'name': 'David'},
        {'id': 'David', 'name': 'Alex'},
        {'id': 'Alex', 'name': 'John'},
    ]
        return JsonResponse(results, safe=False)
    return render(request, 'search.html')