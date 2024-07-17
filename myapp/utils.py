from django.contrib.sessions.models import Session
from django.utils import timezone


def active_sessions_count():
    # Filter out expired sessions
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    return sessions.count()
