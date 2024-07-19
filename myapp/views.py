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
            title = form.cleaned_data['Title']
            videos=form.cleaned_data['video']
            form.save()
            return render(request, 'video.html',context={'Title':title,'videos':videos})
    else:
        return render(request, 'events.html')
