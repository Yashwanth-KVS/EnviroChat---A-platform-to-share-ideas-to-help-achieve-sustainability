from django.urls import path
from myapp_bosun import views

app_name = 'myapp_bosun'
urlpatterns = [
    path('', views.home, name='home'),
    path('feeds/', views.feed_view, name='feeds'),
    ]



