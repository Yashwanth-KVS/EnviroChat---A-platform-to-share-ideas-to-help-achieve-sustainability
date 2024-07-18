from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('search/', views.search_members, name='search_members'),
    path('details/<int:member_id>/', views.member_details, name='member_details'),
    path('create_page/', views.create_pages, name='create_pages'),
    path('view_pages/', views.view_pages, name='view_pages'),
    path('view_single_page<int:page_id>/', views.go_to_single_page, name='go_to_single_page'),

]
