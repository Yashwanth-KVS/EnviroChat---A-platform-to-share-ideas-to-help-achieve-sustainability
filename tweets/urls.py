from django.urls import path
from tweets import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'tweets'
urlpatterns = [
    # path('profile/', views.profile, name='profile'),
    # path('feed/', views.feed, name='feed'),

    path('User_post/', views.User_post, name='User_post'),
    path('post_response/', views.post_response, name='post_response'),
    # path('post_response/', views.upload_content, name='post_response'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)