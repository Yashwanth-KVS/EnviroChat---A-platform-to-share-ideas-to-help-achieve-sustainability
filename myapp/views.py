from datetime import datetime

from django.shortcuts import render

# Create your views here.


from .models import Followers
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegisterForm, PageCreateForm
from django.http import JsonResponse
from .models import Member, Pages
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


def home(request):
    return render(request, 'home.html')


def aboutus(request):
    return render(request, 'aboutus.html')


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
    query = request.GET.get('query', '')
    results = []
    if query:
        members = Member.objects.filter(first_name__icontains(query))[:5]
        results = [{'id': member.user_id, 'name': member.first_name} for member in members]
    else:
        results = [
            {'id': 1, 'name': 'John Doe'},
            {'id': 2, 'name': 'Jane Smith'},
            {'id': 3, 'name': 'Michael Johnson'},
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

    member = member_data.get(member_id, {'name': 'Unknown', 'age': 'Unknown', 'email': 'Unknown',
                                         'profile_pic': 'https://via.placeholder.com/150',
                                         'cover_pic': 'https://via.placeholder.com/800x200', 'interests': []})
    return render(request, 'details.html', {'member': member})


def create_pages(request):
    if request.method == 'POST':
        form = PageCreateForm(request.POST, request.FILES)
        if form.is_valid():
            new_page = form.save(commit=False)
            now = datetime.datetime.now()
            user_id = Member.objects.filter(user_id = 1).values_list('id', flat=True)[0]
            print(user_id)
            form.cleaned_data['user_id'] = user_id
            new_page.page_id = int(now.strftime('%Y%m%d%H%M%S')+str(user_id))#+ form.cleaned_data['user_id'])
            new_page.save()
            print(new_page.page_id)
            print(form.cleaned_data['user_id'])
            print(form.cleaned_data['title'])
            print(form.cleaned_data['content'])
            print(form.cleaned_data['about_page'])
            print(form.cleaned_data['title_img'])
            print(form.cleaned_data['about_img'])
            print(form.cleaned_data['content_img'])

            print('Form saved successfully')
            pages = Pages.objects.all().order_by('-updated_at')
            return redirect(request, template_name='view_pages.html', context={'pages': pages})

        else:
            return render(request, template_name='create_page.html', context={'form': form})

    else:
        form = PageCreateForm()
        return render(request, template_name='create_page.html', context={'form': form})


def view_pages(request):
    if request.method == 'GET':
        pages = Pages.objects.all().order_by('-updated_at')
        for page in pages:
            print(page.page_id)
            print(page.title)
            print(page.content)
            print(page.about_page)
            print(page.title_img.url)
            print(page.content_img.url)
            print(page.about_img.url)
        # Render the template with the fetched pages
        return render(request, 'view_pages.html', {'pages': pages})


def go_to_single_page(request, page_id):
    page = Pages.objects.get(pk=page_id)
    return render(request, 'go_to_selected_page.html', {'pages': page})