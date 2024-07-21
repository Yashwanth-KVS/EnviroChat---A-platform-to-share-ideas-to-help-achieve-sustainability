from django.shortcuts import render
from .models import Feeds, Threads, Pages, Posts


def home(request):
    return render(request, 'home.html')

def feed_view(request):
    # Query feeds and related objects
    feed_items = []

    feed_objects = Feeds.objects.all()[:10]  # Fetching top 10 feeds

    for feed in feed_objects:
        # Fetch related threads, pages, and posts for each feed
        threads = feed.threads_related.all()[:3]  # Fetching top 3 related threads
        pages = feed.pages_related.all()[:3]  # Fetching top 3 related pages
        posts = feed.posts_related.all()[:3]  # Fetching top 3 related posts

        # Append to feed_items list
        feed_items.append({
            'feed': feed,
            'threads': threads,
            'pages': pages,
            'posts': posts
        })

    context = {'feed_items': feed_items}

    print(context)

    return render(request, 'feeds.html', context)
