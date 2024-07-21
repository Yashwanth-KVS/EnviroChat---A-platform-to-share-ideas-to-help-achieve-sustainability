from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('feeds/', views.feed_view, name='feeds'),
    ]



