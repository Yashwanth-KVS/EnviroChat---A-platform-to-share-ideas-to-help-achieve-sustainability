from django.shortcuts import render

from myapp.models import Notification
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def notification_list(request):
    notifications = [
        {
            'user_id': 1,
            'message': 'You have a new message.',
            'created_at': '2024-07-14T14:00:00Z',
            'is_read': False,
        },
        {
            'user_id': 2,
            'message': 'A new article has been published.',
            'created_at': '2024-07-14T16:30:00Z',
            'is_read': False,
        },
    ]

    return render(request, 'notification.html', {'notifications': notifications})

