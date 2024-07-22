from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views

app_name = 'myapp'
urlpatterns = [


    path('create_page/', views.create_pages, name='create_pages'),
    path('view_pages/', views.view_pages, name='view_pages'),
    path('view_single_page<int:page_id>/', views.go_to_single_page, name='go_to_single_page'),
    path('add_comment/<int:page_id>/', views.add_comment, name='add_comment'),
    path('add_comment_videos/<int:video_id>/', views.add_comment_videos, name='add_comment_videos'),
    path('page/<int:page_id>/like/', views.like_page, name='like_page'),
    path('page/<int:page_id>/dislike/', views.dislike_page, name='dislike_page'),
    path('page/<int:page_id>/follow/', views.follow_page, name='follow_page'),
    path('video/<int:video_id>/like/', views.like_videos, name='like_videos'),
    path('video/<int:video_id>/dislike/', views.dislike_videos, name='dislike_video'),
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('Contactus/', views.contactus, name='Contactus'),
    path('', views.check_session, name='check_session'),
    path('events/', views.events, name='events'),
    path('myvideos/', views.myvideos, name='myvideos'),
    path('video_feed/', views.streaming, name='steam'),
    path('video',views.video_feed,name='video_feed'),
    path('stop_stream/', views.stop_stream, name='stop_stream'),
    path('delete/<int:video_id>/', views.delete_video, name='delete_video'),
    path('video_detail<int:video_id>/', views.video_detail, name='video_detail'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('search/', views.search_list, name="search"),
    path('search_name/', views.search_name, name="search_name"),
    path('search_details/<int:id>', views.search_detail, name="search_name"),
]
