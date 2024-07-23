from .models import SiteVisit


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

    class ActiveSessionMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response

        def __call__(self, request):
            response = self.get_response(request)
            request.session.modified = True
            return response
