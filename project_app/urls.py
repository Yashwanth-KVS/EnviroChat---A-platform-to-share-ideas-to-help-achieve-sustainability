from django.urls import path
from . import views

app_name = 'project_app'
urlpatterns = [path('', views.home, name="home"),
               path('feeds/', views.feeds, name="feeds"),
               ]