from django.shortcuts import render
from .models import Feeds


def home(request):
    return render(request,'project_app/home.html',)
# Create your views here.

def feeds(request):
    feeds = Feeds.objects.all()  #Fetch all feeds
    return render(request, 'project_app/feeds.html', {'feeds':feeds})