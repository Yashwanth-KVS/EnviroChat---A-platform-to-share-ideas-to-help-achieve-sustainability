from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from .forms import VideoUploadForm


# Create your views here.

def home(request):
    return render(request, 'home.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def events(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['Title']
            videos = form.cleaned_data['video']
            form.save()
            #return render(request, 'video.html', context={'Title': title, 'videos': videos})
            return HttpResponseRedirect(reverse('video'))
        else:
            return render(request, 'events.html', {'form': form})
    else:
        form = VideoUploadForm()
        return render(request, 'events.html')
