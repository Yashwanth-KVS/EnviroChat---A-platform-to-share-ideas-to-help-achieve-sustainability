from datetime import datetime

from django.shortcuts import render
from .models import Followers
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegisterForm
from django.http import JsonResponse
from .models import Member
from django.shortcuts import render

import datetime


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
# views.py
from django.shortcuts import render, redirect

# views.py
# views.py
from django.shortcuts import render, redirect

# views.py
from django.shortcuts import render, redirect


def search_members(request):
    query = request.GET.get('query', '')
    results = []
    if query:
        members = Member.objects.filter(first_name__icontains(query))[:5]
        results = [{'id': member.user_id, 'name': member.first_name} for member in members]
    else:
        results = [
            {'id': 1, 'name': 'Michael Johnson'},
            {'id': 2, 'name': 'John Doe'},
            {'id': 3, 'name': 'Jane Smith'},
            {'id': 4, 'name': 'Emily Davis'},
            {'id': 5, 'name': 'David Brown'},
        ]
    return render(request, 'search.html', {'results': results, 'query': query})


def member_details(request, member_id):
    # Static data for demonstration
    member_data = {
        1: {'name': 'John Doe', 'age': 30, 'email': 'john@example.com',
            'profile_pic': 'https://randomuser.me/api/portraits/men/1.jpg',
            'cover_pic': 'https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0',
            'interests': ['Reading', 'Traveling', 'Swimming']},
        2: {'name': 'Jane Smith', 'age': 25, 'email': 'jane@example.com',
            'profile_pic': 'https://randomuser.me/api/portraits/women/2.jpg',
            'cover_pic': 'https://images.unsplash.com/photo-1513836279014-a89f7a76ae86',
            'interests': ['Cooking', 'Hiking', 'Gardening']},
        3: {'name': 'Michael Johnson', 'age': 28, 'email': 'michael@example.com',
            'profile_pic': 'https://randomuser.me/api/portraits/men/3.jpg',
            'cover_pic': 'https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0',
            'interests': ['Cycling', 'Photography', 'Gaming']},
        4: {'name': 'Emily Davis', 'age': 22, 'email': 'emily@example.com',
            'profile_pic': 'https://randomuser.me/api/portraits/women/4.jpg',
            'cover_pic': 'https://images.unsplash.com/photo-1513836279014-a89f7a76ae86',
            'interests': ['Painting', 'Running', 'Yoga']},
        5: {'name': 'David Brown', 'age': 35, 'email': 'david@example.com',
            'profile_pic': 'https://randomuser.me/api/portraits/men/5.jpg',
            'cover_pic': 'https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0',
            'interests': ['Writing', 'Fishing', 'Golfing']},
    }

    mutual_followers = [
        {'name': 'Alice Johnson', 'profile_pic': 'https://randomuser.me/api/portraits/women/5.jpg'},
        {'name': 'Bob Smith', 'profile_pic': 'https://randomuser.me/api/portraits/men/6.jpg'},
        {'name': 'Carol Williams', 'profile_pic': 'https://randomuser.me/api/portraits/women/6.jpg'},
    ]

    member = member_data.get(member_id, {'name': 'Unknown', 'age': 'Unknown', 'email': 'Unknown',
                                         'profile_pic': 'https://via.placeholder.com/150',
                                         'cover_pic': 'https://via.placeholder.com/800x200', 'interests': []})
    return render(request, 'details.html', {'member': member, 'mutual_followers': mutual_followers})


def follow_member(request):
    if request.method == 'POST':
        # Handle the follow logic here
        print(f"Followed member with id: {request.POST['member_id']}")
        return redirect('myapp:member_details',
                        member_id=request.POST['member_id'])  # Redirect back to the details page
    return redirect('myapp:search_members')
