from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')


def aboutus(request):
    return render(request, 'aboutus.html')

def events(request):
    return render(request, 'events.html')
