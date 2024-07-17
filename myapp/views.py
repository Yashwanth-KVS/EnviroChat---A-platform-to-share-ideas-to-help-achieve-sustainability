from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils import timezone
from .utils import active_sessions_count
import random
from datetime import datetime, timedelta

from myapp.models import SiteVisit


# Create your views here.

def home(request):
    total_visits = request.session.get('total_visits', 0)
    # site_visit = SiteVisit.objects.get(id=1)
    # global_visit_count = site_visit.visit_count
    # print(site_visit.visit_count)
    # print(f"Global visit count: {global_visit_count}")
    if 'view_count' in request.session:
        request.session['view_count'] += 1
    else:
        request.session['view_count'] = 1

    view_count = request.session['view_count']
    active_sessions = active_sessions_count()
    # print("viewcount", view_count)
    return render(request, 'home.html', {'view_count': view_count, 'active_sessions': active_sessions})


def aboutus(request):
    return render(request, 'aboutus.html')



