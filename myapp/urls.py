from django.urls import path
from myapp import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('Followers/', views.followers_view, name='followers'),
    path('search/', views.search_members, name='search_members'),

]
