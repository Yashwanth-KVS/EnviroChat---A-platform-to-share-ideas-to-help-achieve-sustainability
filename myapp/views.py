import uuid
from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .utils import active_sessions_count
import random
from datetime import datetime, timedelta
from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

# Create your views here.


from .models import Followers
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegisterForm, PageCreateForm
from django.http import JsonResponse
from .models import Member, Pages, Pages_comments, Pages_followers, SiteVisit, SessionCount
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
    goals = [
        {"title": "Foster a Strong Community",
         "description": "Create a vibrant online community where individuals passionate about environmental issues "
                        "can connect, share experiences, and build lasting relationships."
         },
        {"title": "Facilitate Knowledge Exchange",
         "description": "Provide a platform for members to share articles, resources, and insights on various environmental topics, promoting continuous learning and awareness."},
        {"title": "Encourage Collaborative Initiatives",
         "description": "Support and promote collaborative projects and initiatives that aim to address environmental challenges and promote sustainable practices."},
        {"title": "Raise Environmental Awareness",
         "description": "Launch and support awareness campaigns that educate the public about pressing environmental issues and inspire positive action."},
        {"title": "Enhance Accessibility to Resources",
         "description": "Curate and provide easy access to valuable resources, including research papers, toolkits, and best practices for sustainability and environmental conservation."},
        {"title": "Advocate for Policy Change",
         "description": "Mobilize the community to advocate for environmental policies and influence decision-makers to implement sustainable practices and regulations."}
    ]
    total_visits = request.session.get('total_visits', 0)
    site_visit, created = SiteVisit.objects.get_or_create(id=1)
    site_visit.visit_count += 1
    site_visit.save()
    print(f"Updated global visit count to: {site_visit.visit_count}")
    view_count = site_visit.visit_count
    # if 'view_count' in request.session:
    #     request.session['view_count'] += 1
    # else:
    #     request.session['view_count'] = 1
    #
    # view_count = request.session['view_count']
    # print(response)
    active_sessions = active_sessions_count()
    # print("viewcount", view_count)
    return render(request, 'home.html', {'view_count': view_count, 'active_sessions': active_sessions
        , 'goals': goals})


def aboutus(request):
    return render(request, 'aboutus.html')


# def goals_view(request):
#
#     return render(request, 'home.html', {'goals': goals})


def contactus(request):
    team = [
        {
            "name": "Himadhar Reddy Marreddy",
            "email": "mareddyh@uwindsor.ca",
            "linkedin": "https://www.linkedin.com/in/himadhar-mareddy-3bb482295/",
            "image": "images/alice.jpg"
        },
        {
            "name": "Bosun Oke",
            "email": "oke1@uwindsor.ca",
            "linkedin": "https://www.linkedin.com/in/bosunoke/",
            "image": "images/bob.jpg"
        },

        {
            "name": "Yashwanth Kukkala",
            "email": "kukkala1@uwindsor.ca",
            "linkedin": "https://www.linkedin.com/in/yashwanth-kvs-878027104/",
            "image": "images/diana.jpg"
        },
        {
            "name": "Mohammad Ammar",
            "email": "ammar31@uwindsor.ca",
            "linkedin": "https://www.linkedin.com/in/mohammad-ammar31/",
            "image": "images/ethan.jpg"
        },
        {
            "name": "Kavya Chirag Shah",
            "email": "shah7u1@uwindsor.ca",
            "linkedin": "https://www.linkedin.com/in/kavya-shah-be/",
            "image": "images/fiona.jpg"
        },
        {
            "name": "Anjani Kumar Kandula",
            "email": "kandula@uwindsor.ca",
            "linkedin": "https://www.linkedin.com/in/akkandula/",
            "image": "images/george.jpg"
        },
        {
            "name": "Subhram Satyajeet",
            "email": "satyaje@uwindsor.ca",
            "linkedin": "https://www.linkedin.com/in/subhramsatyajeet/",
            "image": "images/charlie.jpg"
        },
        {
            "name": "Bhavisha Dineshbhai Joshi",
            "email": "joshi9f@uwindsor.ca",
            "linkedin": "https://www.linkedin.com/in/bhavisha-joshi-0b56aa173/",
            "image": "images/hannah.jpg"
        }
    ]
    return render(request, 'Contactus.html', {'team': team})


# def get_active_sessions(request):
#     # Filter sessions that have not expired
#     active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
#
#     # Extract session keys and other desired info
#     sessions_data = []
#     for session in active_sessions:
#         data = {
#             'session_key': session.session_key,
#             'expire_date': session.expire_date,
#             # Add more session details if needed
#         }
#         sessions_data.append(data)
#
#     return JsonResponse({'active_sessions': sessions_data})


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
    print(page)
    page_filtered_comments = []
    num_upvotes = 0
    num_downvotes = 0
    page_comments = Pages_comments.objects.filter(page_id = page_id).values()
    for single_page in page_comments:
        if single_page['comment']:
            page_filtered_comments.append(single_page)
            print(single_page)
            user_name = Member.objects.get(pk = single_page['user_id_id']).first_name
            single_page['user_name'] = user_name
        if single_page['upvote'] == 0:
            num_upvotes += 1
        if single_page['downvote'] == 0:
            num_downvotes += 1
    return render(request, 'go_to_selected_page.html', {'page': page, 'page_comments': page_filtered_comments, 'num_upvotes':num_upvotes, 'num_downvotes':num_downvotes})


def like_page(request, page_id):
    page = get_object_or_404(Pages, pk=page_id)
    author = Member.objects.get(pk=1)
    num_upvotes = 0
    Pages_comments.objects.create(page_id=page, user_id=author, upvote=0)
    pages_likes = Pages_comments.objects.filter(page_id = page_id).values()
    for page_com in pages_likes:
        if page_com['upvote'] == 0:
            num_upvotes += 1
    return JsonResponse({'likes': num_upvotes})

def dislike_page(request, page_id):
    page = get_object_or_404(Pages, pk=page_id)
    author = Member.objects.get(pk=1)
    num_downvotes = 0
    Pages_comments.objects.create(page_id=page, user_id=author, upvote=0)
    pages_likes = Pages_comments.objects.filter(page_id = page_id).values()
    for page_com in pages_likes:
        if page_com['downvote'] == 0:
            num_downvotes += 1
    return JsonResponse({'dislikes': num_downvotes})

def add_comment(request, page_id):
    page = get_object_or_404(Pages, pk=page_id)
    if request.method == 'POST':
        comment = request.POST.get('text')
        # author = request.user.username if request.user.is_authenticated else 'Anonymous'
        author = Member.objects.get(pk=1)
        now = datetime.datetime.now()
        # comment_id = int(str(author.user_id)+str(page.page_id))
        Pages_comments.objects.create(page_id=page, user_id=author, comment=comment)
    return redirect('myapp:go_to_single_page', page_id=page.page_id)

def follow_page(request, page_id):
    page = get_object_or_404(Pages, pk=page_id)
    if request.method == 'POST':
        author = Member.objects.get(pk=1)
        Pages_followers.objects.create(page_id=page, follower_id=author)
        num_pages_followers = Pages_followers.objects.filter(page_id=page).values()
        followed_by = num_pages_followers.count()
        return JsonResponse({'followed by': followed_by})

def check_session(request):
    # Check if the cookie is present
    print("Checking session...")
    if 'session_cookie' in request.COOKIES:
        # Cookie exists, do not count the session
        print("Cookie exists. Fetching session count.")
        session_count = SessionCount.objects.first()
        print(session_count)
    else:
        print("Cookie does not exist. Counting session.")
        # Cookie does not exist, count the session
        session_count, created = SessionCount.objects.get_or_create(id=1)  # Using a fixed id for simplicity
        session_count.increment_count()

        # Set the cookie
        response = render(request, 'home.html')
        response.set_cookie('session_cookie', 'exists', max_age=3600)  # Cookie lasts for 1 hour
        return response

    return render(request, 'home.html', {'session_count': session_count})

