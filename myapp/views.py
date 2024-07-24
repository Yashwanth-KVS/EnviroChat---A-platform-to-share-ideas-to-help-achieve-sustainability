import uuid
from datetime import datetime

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import StreamingHttpResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import View

from .utils import active_sessions_count
import random
from datetime import datetime, timedelta
from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetConfirmView, LoginView, PasswordResetView
from django.contrib.auth import logout as auth_logout

# Create your views here.


from .models import Followers
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegisterForm, PageCreateForm, VideoUploadForm, ContentUploadForm
from django.http import JsonResponse
from .models import Member, Pages, Pages_comments, Pages_followers, SiteVisit, SessionCount, Video, Video_comments, Feeds, MediaContent, UserSession, Notifications

from django.shortcuts import render
from myapp.video import VideoCamera, IPWebCam

import datetime
from django.http import HttpResponseServerError
import traceback
import logging
from .video import VideoCamera

logger = logging.getLogger(__name__)


def register(request):
    logger.debug("Register view called")
    if request.method == 'POST':
        logger.debug("POST request received in register view")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            logger.debug("Form is valid in register view")
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            logger.debug(f"Account created for {username}")
            return redirect('myapp:login')
    else:
        logger.debug("GET request received in register view")
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('myapp:home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('myapp:login')

    def form_valid(self, form):
        messages.success(self.request, 'Your password was successfully changed.')
        return super().form_valid(form)


class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_url = reverse_lazy('myapp:password_reset_done')
    success_message = "Password reset link has been sent to your email."


def home(request):
    goals = [
        {"title": "Foster a Strong Community",
         "description": "Create a vibrant online community where individuals passionate about environmental issues "
                        "can connect, share experiences, and build lasting relationships."
         },
        {"title": "Facilitate Knowledge Exchange",
         "description": "Provide a platform for members to share articles, resources, and insights on various environmental topics, promoting continuous learning and awareness."},
        {"title": "Encourage Collaborative Initiatives",
         "description": "Support and promote collaborative projects and initiatives that aim to address environmental challenges and promote sustainable practices."},
        {"title": "Raise Environmental Awareness",
         "description": "Launch and support awareness campaigns that educate the public about pressing environmental issues and inspire positive action."},
        {"title": "Enhance Accessibility to Resources",
         "description": "Curate and provide easy access to valuable resources, including research papers, toolkits, and best practices for sustainability and environmental conservation."},
        {"title": "Advocate for Policy Change",
         "description": "Mobilize the community to advocate for environmental policies and influence decision-makers to implement sustainable practices and regulations."}
    ]
    total_visits = request.session.get('total_visits', 0)
    site_visit, created = SiteVisit.objects.get_or_create(id=1)
    site_visit.visit_count += 1
    site_visit.save()
    print(f"Updated global visit count to: {site_visit.visit_count}")
    view_count = site_visit.visit_count
    # if 'view_count' in request.session:
    #     request.session['view_count'] += 1
    # else:
    #     request.session['view_count'] = 1
    #
    # view_count = request.session['view_count']
    # print(response)
    active_sessions = active_sessions_count()
    # print("viewcount", view_count)
    return render(request, 'home.html', {'view_count': view_count, 'active_sessions': active_sessions
        , 'goals': goals, 'user': request.user})


def aboutus(request):
    return render(request, 'aboutus.html')


# def goals_view(request):
#
#     return render(request, 'home.html', {'goals': goals})


def contactus(request):
    team = [
        {
            "name": "Himadhar Reddy Marreddy",
            "email": "mareddyh@uwindsor.ca",
            "linkedin": "https://www.linkedin.com/in/himadhar-mareddy-3bb482295/",
            "image": "images/alice.jpg"
        },
        {
            "name": "Bosun Oke",
            "email": "oke1@uwindsor.ca",
            "linkedin": "https://www.linkedin.com/in/bosunoke/",
            "image": "images/bob.jpg"
        },

        {
            "name": "Yashwanth Kukkala",
            "email": "kukkala1@uwindsor.ca",
            "linkedin": "https://www.linkedin.com/in/yashwanth-kvs-878027104/",
            "image": "images/diana.jpg"
        },
        {
            "name": "Mohammad Ammar",
            "email": "ammar31@uwindsor.ca",
            "linkedin": "https://www.linkedin.com/in/mohammad-ammar31/",
            "image": "images/ethan.jpg"
        },
        {
            "name": "Kavya Chirag Shah",
            "email": "shah7u1@uwindsor.ca",
            "linkedin": "https://www.linkedin.com/in/kavya-shah-be/",
            "image": "images/fiona.jpg"
        },
        {
            "name": "Anjani Kumar Kandula",
            "email": "kandula@uwindsor.ca",
            "linkedin": "https://www.linkedin.com/in/akkandula/",
            "image": "images/george.jpg"
        },
        {
            "name": "Subhram Satyajeet",
            "email": "satyaje@uwindsor.ca",
            "linkedin": "https://www.linkedin.com/in/subhramsatyajeet/",
            "image": "images/charlie.jpg"
        },
        {
            "name": "Bhavisha Dineshbhai Joshi",
            "email": "joshi9f@uwindsor.ca",
            "linkedin": "https://www.linkedin.com/in/bhavisha-joshi-0b56aa173/",
            "image": "images/hannah.jpg"
        }
    ]
    return render(request, 'Contactus.html', {'team': team})


# def get_active_sessions(request):
#     # Filter sessions that have not expired
#     active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
#
#     # Extract session keys and other desired info
#     sessions_data = []
#     for session in active_sessions:
#         data = {
#             'session_key': session.session_key,
#             'expire_date': session.expire_date,
#             # Add more session details if needed
#         }
#         sessions_data.append(data)
#
#     return JsonResponse({'active_sessions': sessions_data})

@login_required()
def create_pages(request):
    if request.method == 'POST':
        # if request.user.is_authenticated:
        #     pass
        # else:
        #     return redirect('myapp:login')
        form = PageCreateForm(request.POST, request.FILES)
        if form.is_valid():
            new_page = form.save(commit=False)
            now = datetime.datetime.now()
            #user_id = Member.objects.filter(user_id=1).values_list('id', flat=True)[0]
            # if request.user.is_authenticated:
            user_id = request.user.id

            print("///////////////////////////")
            print(user_id)
            form.cleaned_data['user_id'] = user_id
            new_page.page_id = int(now.strftime('%Y%m%d%H%M%S')) #+ str(user_id))  #+ form.cleaned_data['user_id'])
            new_page.save()
            print(new_page.page_id)
            print(form.cleaned_data['user_id'])
            print(form.cleaned_data['title'])
            print(form.cleaned_data['content'])
            print(form.cleaned_data['about_page'])
            print(form.cleaned_data['title_img'])
            print(form.cleaned_data['about_img'])
            print(form.cleaned_data['content_img'])

            print('Form saved successfully')
            pages = Pages.objects.all().order_by('-updated_at')
            #return redirect(request, template_name='view_pages.html', context={'pages': pages})
            return redirect(reverse('myapp:view_pages'))

        else:
            #return render(request, template_name='create_page.html', context={'form': form})
            return redirect(reverse('myapp:view_pages'))

    else:
        form = PageCreateForm()
        return render(request, template_name='create_page.html', context={'form': form})
        #return redirect(reverse('myapp:view_pages'))


def view_pages(request):
    if request.method == 'GET':
        pages = Pages.objects.all().order_by('-updated_at')
        for page in pages:
            print(page.page_id)
            print(page.title)
            print(page.content)
            print(page.about_page)
            print(page.title_img.url)
            print(page.content_img.url)
            print(page.about_img.url)
        # Render the template with the fetched pages
        print(pages)
        return render(request, 'view_pages.html', {'pages': pages})


def go_to_single_page(request, page_id):
    page = Pages.objects.get(pk=page_id)
    print(page)
    page_filtered_comments = []
    num_upvotes = 0
    num_downvotes = 0
    page_comments = Pages_comments.objects.filter(page_id=page_id).values()
    for single_page in page_comments:
        if single_page['comment']:
            page_filtered_comments.append(single_page)
            print(single_page)
            user_name = Member.objects.get(pk=single_page['user_id_id']).first_name
            single_page['user_name'] = user_name
        if single_page['upvote'] == 0:
            num_upvotes += 1
        if single_page['downvote'] == 0:
            num_downvotes += 1
    return render(request, 'go_to_selected_page.html',
                  {'page': page, 'page_comments': page_filtered_comments, 'num_upvotes': num_upvotes,
                   'num_downvotes': num_downvotes})


def like_page(request, page_id):
    page = get_object_or_404(Pages, pk=page_id)
    author = Member.objects.get(pk=1)
    num_upvotes = 0
    Pages_comments.objects.create(page_id=page, user_id=author, upvote=0)
    Notifications.create_page_like_notification(sender=author)
    pages_likes = Pages_comments.objects.filter(page_id=page_id).values()
    for page_com in pages_likes:
        if page_com['upvote'] == 0:
            num_upvotes += 1
    return JsonResponse({'likes': num_upvotes})


def dislike_page(request, page_id):
    page = get_object_or_404(Pages, pk=page_id)
    author = Member.objects.get(pk=1)
    dislikes = 0
    Pages_comments.objects.create(page_id=page, user_id=author, upvote=0)
    Notifications.create_page_dislike_notification(sender=author)
    pages_likes = Pages_comments.objects.filter(page_id=page_id).values()
    for page_com in pages_likes:
        if page_com['downvote'] == 0:
            dislikes += 1
    return JsonResponse({'dislikes': dislikes})


def add_comment(request, page_id):
    page = get_object_or_404(Pages, pk=page_id)
    if request.method == 'POST':
        comment = request.POST.get('text')
        author = request.user.id if request.user.is_authenticated else 'Anonymous'
        author = Member.objects.get(pk=1)
        now = datetime.datetime.now()
        # comment_id = int(str(author.user_id)+str(page.page_id))
        Pages_comments.objects.create(page_id=page, user_id=author, comment=comment)
        Notifications.create_page_comment_notification(sender=author)
    return redirect('myapp:go_to_single_page', page_id=page.page_id)


def follow_page(request, page_id):
    page = get_object_or_404(Pages, pk=page_id)
    if request.method == 'POST':
        author = Member.objects.get(pk=1)
        Pages_followers.objects.create(page_id=page, follower_id=author)
        Notifications.create_follow_notification(sender=author)
        num_pages_followers = Pages_followers.objects.filter(page_id=page).values()
        followed_by = num_pages_followers.count()
        return JsonResponse({'followed by': followed_by})


def check_session(request):
    # Check if the cookie is present
    print("Checking session...")
    if 'session_cookie' in request.COOKIES:
        # Cookie exists, do not count the session
        print("Cookie exists. Fetching session count.")
        session_count = SessionCount.objects.first()
        print(session_count)
    else:
        print("Cookie does not exist. Counting session.")
        # Cookie does not exist, count the session
        session_count, created = SessionCount.objects.get_or_create(id=1)  # Using a fixed id for simplicity
        session_count.increment_count()

        # Set the cookie
        response = render(request, 'home.html')
        response.set_cookie('session_cookie', 'exists', max_age=3600)  # Cookie lasts for 1 hour
        return response

    return render(request, 'home.html', {'session_count': session_count})

@login_required()
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
    print("myvideos")
    videos = Video.objects.all()
    return render(request, 'video.html', {'videos': videos, 'media_url': settings.MEDIA_URL})

@login_required()
def delete_video(request, video_id):
    print('delete_video')
    video = get_object_or_404(Video, pk=video_id)
    if request.method == 'POST':
        video.delete()
        print('Video deleted')
        # Optionally, redirect to a different URL after deletion
        return redirect('myapp:myvideos')
    # Handle GET request (if any)
    return redirect('myapp:myvideos')


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
            camera = VideoCamera()  # Initialize the camera if not already initialized

        return StreamingHttpResponse(gen(camera), content_type='multipart/x-mixed-replace; boundary=frame')

    except Exception as e:
        traceback.print_exc()  # Print traceback to console for debugging
        return HttpResponseServerError('Internal Server Error')


def video_detail(request, video_id):
    video = Video.objects.filter(video_id=video_id).values()
    return render(request, 'video_detail.html', {'video': video, 'media_url': settings.MEDIA_URL})

@login_required()
def streaming(request):
    return render(request, 'video_stream.html')


def stop_stream(request):
    global camera
    try:
        if camera is not None:
            del camera  # Release the camera instance
            camera = None  # Reset camera variable to None
        #return render(request, 'home.html')
        return home(request)

    except Exception as e:
        print(e)
        return HttpResponse('Failed to stop stream', status=500)


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@login_required()
def like_videos(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    author = Member.objects.get(pk=1)
    num_upvotes = 0
    Video_comments.objects.create(video_id=video, user_id=author, upvote=0)
    video_likes = Video_comments.objects.filter(video_id=video_id).values()
    Notifications.create_video_like_notification(sender=author)
    for page_com in video_likes:
        if page_com['upvote'] == 0:
            num_upvotes += 1
    return JsonResponse({'likes': num_upvotes})

@login_required()
def dislike_videos(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    author = Member.objects.get(pk=1)
    dislikes = 0
    Video_comments.objects.create(video_id=video, user_id=author, upvote=0)
    video_likes = Video_comments.objects.filter(video_id=video_id).values()
    Notifications.create_video_dislike_notification(sender=author)
    for page_com in video_likes:
        if page_com['downvote'] == 0:
            dislikes += 1
    return JsonResponse({'dislikes': dislikes})

@login_required()
def add_comment_videos(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    print(video)
    if request.method == 'POST':
        comment = request.POST.get('text')
        # author = request.user.username if request.user.is_authenticated else 'Anonymous'
        author = Member.objects.get(pk=1)
        now = datetime.datetime.now()
        # comment_id = int(str(author.user_id)+str(page.page_id))
        Video_comments.objects.create(video_id=video, user_id=author, comment=comment)
        Notifications.create_video_comment_notification(sender=author)
        print(video.video_id)
    return redirect('myapp:video_detail', video_id=video.video_id)


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def search_list(request):
    return render(request, 'search.html')


def search_name(request):
    query = request.GET.get('search', '')
    objs = Member.objects.filter(username__startswith=query)
    payload = []
    for obj in objs:
        payload.append({
            'id': obj.id,
            'name': obj.username
        })
    return JsonResponse({
        'status': True,
        'payload': payload
    })


def search_detail(request, id):
    mem = get_object_or_404(Member, id=id)
    return render(request, "search-details.html", {"member": mem})

def feed_view(request):
    # Query feeds and related objects
    feed_items = []

    feed_objects = Feeds.objects.all()[:10]  # Fetching top 10 feeds

    for feed in feed_objects:
        # Fetch related threads, pages, and posts for each feed
        threads = feed.threads_related.all()[:10]  # Fetching top 3 related threads
        pages = feed.pages_related.all().values()[:10]  # Fetching top 3 related pages
        #pages = Pages.objects.all()
        #posts = feed.posts_related.all()[:3]  # Fetching top 3 related posts
        print(pages)
        # Append to feed_items list
        feed_items.append({
            'feed': feed,
            'threads': threads,
            'pages': pages,
            #'posts': posts
        })

    context = {'feed_items': feed_items}

    print(context)

    return render(request, 'feeds.html', context)

@login_required()
def User_post(request):
    print("entered")
    print(request)
    if request.method == 'POST':
        print("entered post")
        form = ContentUploadForm(request.POST, request.FILES)

        if form.is_valid():
            new_post = form.save(commit=False)
            print(form.cleaned_data['content'])
            print(form.cleaned_data['image'])
            print("entered valid")
            # media_content = MediaContent(
            #     content=form.cleaned_data['content'],
            #     image=form.cleaned_data.get('image'),
            #     video=form.cleaned_data.get('video')
            # )
            # print(media_content)
            # media_content.save()
            new_post.save()

            return redirect('myapp:post_response')
    else:
        print("entered else")
        form = ContentUploadForm()
    return render(request, 'User_post.html', {'form': form})


class vote(View):
    @staticmethod
    def post(request, content_id):
        content = get_object_or_404(MediaContent, id=content_id)
        action = request.POST.get('action')

        if action == 'upvote':
            content.likes += 1
        elif action == 'downvote':
            content.dislikes += 1

        content.save()
        return redirect('post_responses')


def post_response(request):
    print("entered post_resp")
    posts = MediaContent.objects.all()
    return render(request, 'post_response.html', {'posts': posts})


def user_logout(request):
    if request.method == "POST":
        auth_logout(request)
        messages.add_message(
            request,
            messages.SUCCESS,
            "You have successfully logged out !!",
            extra_tags="success",
        )
        return redirect("myapp:login")
    return redirect("myapp:dashboard")


def tedtalk(request):
    return render(request,'tedplay.html')



@login_required
def login_history(request):
    all_history = UserSession.objects.filter(user=request.user).order_by('-created_at')
    one_day_ago = UserSession.objects.filter(user=request.user, created_at__gte=timezone.now() - timedelta(days=1))
    seven_day_ago = UserSession.objects.filter(user=request.user, created_at__gte=timezone.now() - timedelta(days=7))
    return render(request, 'login_history.html', {
        'all_history': all_history,
        'title': 'Login History',
        'one_day_ago': one_day_ago,
        'seven_day_ago': seven_day_ago
    })


@login_required()
def delete_page(request, page_id):
    print('delete_page')
    page = get_object_or_404(Pages, pk=page_id)
    if request.method == 'POST':
        page.delete()
        print('Page deleted')
        # Optionally, redirect to a different URL after deletion
        return redirect('myapp:view_pages')
    # Handle GET request (if any)
    return redirect('myapp:view_pages')

@login_required()
def notifications_list(request):
    notifications = Notifications.objects.all().order_by('-created_at')
    return render(request, 'notification_page.html', {'notifications':notifications})