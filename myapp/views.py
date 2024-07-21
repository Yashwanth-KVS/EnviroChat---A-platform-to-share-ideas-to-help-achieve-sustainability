from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils import timezone
from .utils import active_sessions_count
import random
from datetime import datetime, timedelta
from django.http import JsonResponse
from myapp.models import SiteVisit

# Create your views here.


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
                                         ,'goals': goals})


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
