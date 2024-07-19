from django.shortcuts import render,redirect
from .forms import VideoUploadForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


def aboutus(request):
    return render(request, 'aboutus.html')

def events(request):
    if request.method == 'POST':
        form=VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render((request, 'events.html')
    else:
        return render(request, 'events.html')
