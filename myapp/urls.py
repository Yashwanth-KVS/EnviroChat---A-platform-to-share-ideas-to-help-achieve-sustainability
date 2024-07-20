from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('search/', views.search_list, name="search"),
    path('search_name/', views.search_name, name="search_name"),
    path('search_details/<int:id>', views.search_detail , name="search_name"),

]
