from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from flask import Response
from myapp.video import VideoCamera,IPWebCam
from .forms import VideoUploadForm
from .models import Video
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseServerError
import traceback

from .video import VideoCamera


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
    return render(request, 'video.html', {'videos': videos, 'media_url': settings.MEDIA_URL})


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


camera = None  # Global variable to hold the camera instance


def video_feed(request):
    global camera
    try:
        if camera is None:
            camera = VideoCamera() # Initialize the camera if not already initialized

        return StreamingHttpResponse(gen(camera), content_type='multipart/x-mixed-replace; boundary=frame')

    except Exception as e:
        traceback.print_exc()  # Print traceback to console for debugging
        return HttpResponseServerError('Internal Server Error')


def streaming(request):
    return render(request, 'video_stream.html')


def stop_stream(request):
    global camera
    try:
        if camera is not None:
            del camera  # Release the camera instance
            camera = None  # Reset camera variable to None
        return HttpResponse('Stream stopped successfully', status=200)

    except Exception as e:
        print(e)
        return HttpResponse('Failed to stop stream', status=500)


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')