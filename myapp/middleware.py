from .models import SiteVisit
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import user_logged_in
from .models import UserSession


class VisitCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Increment global visit counter
        # site_visit, created = SiteVisit.objects.get_or_create(id=1)
        # site_visit.visit_count += 1
        # site_visit.save()
        # print(f"Updated global visit count to: {site_visit.visit_count}")

        return response


def create_user_session(sender, request, user, **kwargs):
    UserSession.objects.create(user=user)


class LoginHistoryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        pass  # This can be left empty or used for other request-based logic


user_logged_in.connect(create_user_session)
