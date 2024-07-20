from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# tweets1/models.py
# tweets1/views.py
from django.contrib.auth.models import User
# from .models import Tweet
from django.shortcuts import render
from .forms import ContentUploadForm

from django.shortcuts import render, redirect
from .forms import ContentUploadForm

from django.shortcuts import render, redirect
from .forms import ContentUploadForm
from .models import MediaContent


def User_post(request):
    print("entered")
    print(request)
    if request.method == 'POST':
        print("entered post")
        form = ContentUploadForm(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data['content'])
            print(form.cleaned_data['image'])
            print("entered valid")
            media_content = MediaContent(
                content=form.cleaned_data['content'],
                image=form.cleaned_data.get('image'),
                video=form.cleaned_data.get('video')
            )
            print(media_content)
            media_content.save()

            return redirect('tweets:post_response')
    else:
        print("entered else")
        form = ContentUploadForm()
    return render(request, 'tweets/User_post.html', {'form': form})


def post_response(request):
    print("entered post_resp")
    posts = MediaContent.objects.all()
    return render(request, 'tweets/post_response.html', {'posts': posts})

# def User_post(request):
#     print("fdflkmdf")
#     if request.method == 'POST':
#         print("passeed post")
#         form = ContentUploadForm(request.POST, request.FILES)
#         print("passed vedio")
#         if form.is_valid():
#             print("passed valid")
#             content = form.cleaned_data.get('content')
#             image = form.cleaned_data.get('image')
#             video = form.cleaned_data.get('video')
#             print(content)
#             media_content = MediaContent(content=content)
#             print(media_content)
#             if image:
#                 media_content.image = image
#             if video:
#                 media_content.video = video
#
#             media_content.save()
#             print(media_content)
#             return redirect('post_response')  # Redirect to the posts page after successful upload
#     else:
#         form = ContentUploadForm()
#     return render(request, 'tweets/User_post.html', {'form': form})
#
#
# def post_response(request):
#     posts = MediaContent.objects.all()
#     posts.media_content = posts
#     return render(request, 'tweets/post_response.html', {'posts': posts})

# def upload_content(request):
#     if request.method == 'POST':
#         form = ContentUploadForm(request.POST, request.FILES)
#         print(form)
#         if form.is_valid():
#             # Process the form data
#             content = form.cleaned_data['content']
#             image = form.cleaned_data['image']
#             video = form.cleaned_data['video']
#
#             # Assuming you want to do something with the uploaded files (e.g., save to database or filesystem)
#             # Handle file processing here if needed
#
#             # Redirect to the response page
#             # return redirect('post_response.html')
#             return render(request, 'tweets/post_response.html', {'content': content})
#     else:
#         form = ContentUploadForm()
#
#     return render(request, 'tweets/User_post.html', {'form': form})

# @login_required
# def feed(request):
#     users = User.objects.all()  # For simplicity, we'll show tweets1 from all users
#     tweets1 = Tweet.objects.filter(user__in=users).order_by('-created_at')
#     return render(request, 'tweets1/feed.html', {'tweets1': tweets1})


# def profile(request):
#     tweets1 = Tweet.objects.filter(user=request.user).order_by('-created_at')
#     return render(request, 'tweets1/profile.html', {'tweets1': tweets1})


# def User_post(request):
#     return render(request, 'tweets1/User_post.html')
