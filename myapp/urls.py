from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('Contactus/', views.contactus, name='Contactus'),
    # path('', views.goals_view, name='goals_view'),
    # path('login/', )
]
