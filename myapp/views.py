from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from .forms import VideoUploadForm
from .models import Video
from django.conf import settings
from django.conf.urls.static import static
# Create your views here.

def home(request):
    return render(request, 'home.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def events(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['Title']
            videos = form.cleaned_data['video']
            form.save()
            return HttpResponseRedirect(reverse('myapp:events'))
        else:
            return render(request, 'events.html', {'form': form})
    else:
        form = VideoUploadForm()
        return render(request, 'events.html')

def myvideos(request):
    videos = Video.objects.all()
    return render(request,'video.html',{'videos':videos,'media_url':settings.MEDIA_URL})

