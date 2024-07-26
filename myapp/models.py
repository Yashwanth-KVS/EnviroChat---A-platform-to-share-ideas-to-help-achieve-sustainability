from random import choices

from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone


class Member(User):
    user_id = models.AutoField(unique=True, primary_key=True)
    # email_id = models.EmailField(unique=True)
    dob = models.DateField(default=datetime.date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='profile_pictures')
    cover_picture = models.ImageField(upload_to='cover_pictures')
    interests = models.TextField(blank=True)

    def __str__(self):
        return str(self.username)


class Followers(models.Model):
    STATUS_CHOICES = [
        (1, 'Request'),
        (2, 'Following'),
    ]
    id = models.AutoField(primary_key=True)
    follower_id = models.ForeignKey(Member, related_name='followers', on_delete=models.CASCADE)
    followee_id = models.ForeignKey(Member, related_name='following', on_delete=models.CASCADE)
    request_id = models.ManyToManyField(Member, related_name='requests')

    def __str__(self):
        return str(self.follower_id)


class Feeds(models.Model):
    # id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(Member, on_delete=models.CASCADE)
    # updated_at = models.DateTimeField(auto_now=True)
    #
    # def __str__(self):
    #     return str(self.id)
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(default=timezone.now)
    threads = models.ManyToManyField('Threads', related_name='feeds_threads', blank=True)
    pages = models.ManyToManyField('Pages', related_name='feeds_pages', blank=True)
    posts = models.ManyToManyField('Posts', related_name='feeds_posts', blank=True)
    videos = models.ManyToManyField('Video', related_name='feeds_videos', blank=True)
    media = models.ManyToManyField('MediaContent', related_name='feeds_media', blank=True)

    class Meta:
        verbose_name_plural = 'Feeds'

    def __str__(self):
        return str(self.id)


class Threads(models.Model):
    STATUS_CHOICES = [
        (1, 'Open'),
        (2, 'Closed'),
    ]
    thread_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    feed = models.ForeignKey(to=Feeds, on_delete=models.CASCADE, related_name="threads_related")  # Only one ForeignKey to Feeds
    category = models.IntegerField(choices=STATUS_CHOICES, default=1)
    query = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Threads'

    def __str__(self):
        return str(self.thread_id)


class ThreadComments(models.Model):
    thread_comment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    thread_id = models.ForeignKey(to=Threads, on_delete=models.CASCADE, default=1)
    comment = models.TextField()
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    feed = models.ForeignKey(Feeds, on_delete=models.CASCADE, related_name='threads_comments', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ThreadComments'

    def __str__(self):
        return str(self.comment)

class Posts(models.Model):
    STATUS_CHOICES = [
        (1, 'Thread'),
        (2, 'Regular Post'),
        (3, 'Video Post'),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    category = models.IntegerField(choices=STATUS_CHOICES, default=2)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    feed = models.ForeignKey(to=Feeds, on_delete=models.CASCADE, related_name="posts_related", default=1)

    def __str__(self):
        return str(self.id)


# class Favorites(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(Member, on_delete=models.CASCADE)
#     post = models.ForeignKey(Posts, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return str(self.id)

class Favorites(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    thread_id = models.ForeignKey(to=Threads, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Favourites'

    def __str__(self):
        return str(self.id)


class FeedsPosts(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feeds, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Pages(models.Model):
    page_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE, blank=True, null=True)
    title = models.TextField()
    content = models.TextField()
    title_img = models.FileField(upload_to='title_imgs',default='title_page.jpg')
    content_img = models.FileField(upload_to='content_imgs', default='content_image.jpg')
    about_page = models.TextField(default='The page promotes discussion base for green energy')
    about_img = models.FileField(upload_to='about_imgs', default='content_page.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    feed = models.ForeignKey(Feeds, on_delete=models.CASCADE, related_name='pages_related',
                             default=1)  # Added default value

    def __str__(self):
        return str(self.page_id)



class Pages_comments(models.Model):
    choices = [
        (0, 'Yes'),
        (1, 'No'),
    ]
    page_id = models.ForeignKey(to=Pages, on_delete=models.CASCADE)
    pages_comment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField()
    upvote = models.IntegerField(choices=choices, default=1)
    downvote = models.IntegerField(choices=choices, default=1)

    def __str__(self):
        return str(self.comment)


class Pages_followers(models.Model):
    id = models.AutoField(primary_key=True)
    page_id = models.ForeignKey(to=Pages, on_delete=models.CASCADE, default=202407171858142)
    follower_id = models.ForeignKey(to=Member, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.id)

class SiteVisit(models.Model):
    visit_count = models.PositiveIntegerField(default=0)


class SessionCount(models.Model):
    count = models.IntegerField(default=0)

    def increment_count(self):
        self.count += 1
        self.save()

class Video(models.Model):
    Title = models.CharField(max_length=255)
    video_id = models.IntegerField(primary_key=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d')
    uploaded_by = models.ForeignKey(to=Member, on_delete=models.CASCADE, null=True, blank=True, default = 1)
    feed = models.ForeignKey(Feeds, on_delete=models.CASCADE, related_name='videos_related',
                             default=1)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.Title)

class Video_comments(models.Model):
    choices = [
        (0, 'Yes'),
        (1, 'No'),
    ]
    video_id = models.ForeignKey(to=Video, on_delete=models.CASCADE)
    video_comment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField()
    upvote = models.IntegerField(choices=choices, default=1)
    downvote = models.IntegerField(choices=choices, default=1)

    def __str__(self):
        return str(self.comment)

class MediaContent(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='images/%y', blank=True, null=True)
    video = models.FileField(upload_to='videos/%y', blank=True, null=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    feed = models.ForeignKey(Feeds, on_delete=models.CASCADE, related_name='media_related',
                             default=1)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"MediaContent {self.id}"




class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)

class Notifications(models.Model):
    NOTIFICATION_TYPES = [
        ('follow', 'Follow Notification'),
        ('post', 'post Notification'),
        ('video_like', 'Video Like Notification'),
        ('post_like', 'Post Like Notification'),
        ('video_comment', 'Video Comment Notification'),
        ('post_comment', 'Post Comment Notification'),
        ('page_comment', 'Page Comment Notification'),
        ('event', 'Event Notification'),
        ('page_like', 'Page like Notification'),
        ('page_dislike', 'Page dislike Notification'),
        ('video_comment', 'Video Comment Notification'),
        ('video_dislike', 'Video disLike Notification'),

    ]

    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True, related_name='notifications_sent')
    notification_type = models.CharField(max_length=15, choices=NOTIFICATION_TYPES)
    message = models.CharField(max_length=128, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return f'Notification {self.id}'

    @classmethod
    def create_follow_notification(cls, sender):
        return cls.objects.create(
            sender=sender,
            notification_type='follow',
            message=f"{sender.first_name} {sender.last_name} - Follow Notification"
        )

    @classmethod
    def create_post_like_notification(cls, sender):
        return cls.objects.create(
            sender=sender,
            notification_type='post_like',
            message=f'{sender.first_name} {sender.last_name} - Post Like Notification'
        )

    @classmethod
    def create_video_comment_notification(cls, sender):
        return cls.objects.create(
            sender=sender,
            notification_type='video_comment',
            message=f'{sender.first_name} {sender.last_name} - Video Comment Notification'
        )

    @classmethod
    def create_post_comment_notification(cls, sender, post):
        notification = cls.objects.create(
            sender=sender,
            notification_type='post_comment',
            message=f'{sender.first_name} {sender.last_name} - Post Comment Notification',
            post=post
        )

    @classmethod
    def create_post_notification(cls,  sender):
        return cls.objects.create(
            sender=sender,
            notification_type='post',
            message=f'{sender.first_name} {sender.last_name} - Post Notification'
        )

    @classmethod
    def create_video_like_notification(cls, sender):
        return cls.objects.create(
            sender=sender,
            notification_type='video_like',
            message=f'{sender.first_name} {sender.last_name} - Video Like Notification'
        )

    @classmethod
    def create_page_comment_notification(cls, sender):
        return cls.objects.create(
            sender=sender,
            notification_type='page_comment',
            message=f'{sender.first_name} {sender.last_name} - Page Comment Notification'
        )

    @classmethod
    def create_event_notification(cls, sender):
        return cls.objects.create(
            sender=sender,
            notification_type='event',
            message=f'{sender.first_name} {sender.last_name} - Event Notification'
        )

    @classmethod
    def create_page_like_notification(cls, sender):
        return cls.objects.create(
            sender=sender,
            notification_type='page like',
            message=f"{sender.first_name} {sender.last_name} - page like Notification"
        )

    @classmethod
    def create_page_dislike_notification(cls, sender):
        return cls.objects.create(
            sender=sender,
            notification_type='page dislike',
            message=f"{sender.first_name} {sender.last_name} - page dislike Notification"
        )

    @classmethod
    def create_video_dislike_notification(cls, sender):
        return cls.objects.create(
            sender=sender,
            notification_type='video_dislike',
            message=f'{sender.first_name} {sender.last_name} - Video disLike Notification'
        )