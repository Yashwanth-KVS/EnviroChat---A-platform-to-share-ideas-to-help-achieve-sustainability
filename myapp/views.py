from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils import timezone
from .utils import active_sessions_count
from .middleware import VisitCounterMiddleware
import random
from datetime import datetime, timedelta
from .models import SiteVisit

from myapp.models import SiteVisit


# Create your views here.


def home(request):
    total_visits = request.session.get('total_visits', 0)
    # site_visit = SiteVisit.objects.get(id=1)
    # global_visit_count = site_visit.visit_count
    # print(site_visit.visit_count)
    # print(f"Global visit count: {global_visit_count}")
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
    return render(request, 'home.html', {'view_count': view_count, 'active_sessions': active_sessions})


def aboutus(request):
    return render(request, 'aboutus.html')


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



