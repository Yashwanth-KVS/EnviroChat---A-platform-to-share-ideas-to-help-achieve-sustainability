from django.shortcuts import render
from .models import Followers


# Create your views here.
def followers(request):
    follow_request = followers.objects.filter(STATUS_CHOICES=1)
    context = {'latest_tweets': latest_tweets}
    return render(request, 'myapp/templates/myapp/tweet.html', context)