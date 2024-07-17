from django.urls import path
from myapp import views
app_name = 'myapp'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('search/', views.search_members, name='search_members'),
    path('details/<int:member_id>/', views.member_details, name='member_details'),
    path('follow/', views.follow_member, name='follow_member'),
    ]

