from django.urls import path
from tweets import views
from django.conf import settings
from django.conf.urls.static import static

from tweets.views import vote

app_name = 'tweets'
'tweets: vote'

urlpatterns = [
    # path('profile/', views.profile, name='profile'),
    # path('feed/', views.feed, name='feed'),

    path('User_post/', views.User_post, name='User_post'),
    path('vote/<int:content_id>/', vote.as_view(), name='vote'),
    path('post_response/', views.post_response, name='post_response'),
    # path('post_response/', views.upload_content, name='post_response'),
]


