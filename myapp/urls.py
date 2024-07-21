from django.template.context_processors import static
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from EnviroChat import settings
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('events/', views.events, name='events'),
    path('myvideos/', views.myvideos, name='myvideos'),
    path('video_feed/', views.streaming, name='steam'),
    path('video',views.video_feed,name='video_feed'),
    path('stop_stream/', views.stop_stream, name='stop_stream'),
    path('delete/<int:video_id>/', views.delete_video, name='delete_video'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)