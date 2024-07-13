from random import choices

from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone


class Member(User):
    user_id = models.IntegerField(unique=True, primary_key=True)
    email_id = models.EmailField(unique=True)
    dob = models.DateField(default=datetime.date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='profile_pictures')
    cover_picture = models.ImageField(upload_to='cover_pictures')
    interests = models.TextField(blank=True)

    def __str__(self):
        return self.first_name


class Followers(models.Model):
    id = models.IntegerField(primary_key=True)
    follower_id = models.ManyToManyField(Member, related_name='followers')
    followee_id = models.ManyToManyField(Member, related_name='following')

    def __str__(self):
        return str(self.id)


class feeds(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Threads(models.Model):
    thread_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    #category = models.IntegerField(choices=STATUS_CHOICES, default=2)
    query = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class ThreadComments(models.Model):
    choices = [
        (0, 'Yes'),
        (1, 'No'),
    ]
    thread_comment_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    comment = models.TextField()
    upvote = models.IntegerField(choices=choices, default=0)
    downvote = models.IntegerField(choices=choices, default=0)

    def __str__(self):
        return str(self.comment)


class Favorites(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    #thread_id = models.ForeignKey(to=Posts, on_delete=models.CASCADE)
    thread_id = models.ForeignKey(to=Threads, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class feeds_posts(models.Model):
    id = models.IntegerField(primary_key=True)
    #post_id = models.ForeignKey(to=Posts, on_delete=models.CASCADE)
    thread_id = models.ForeignKey(to=Threads, on_delete=models.CASCADE)
    feed_id = models.ForeignKey(to=feeds, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Pages(models.Model):
    page_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

class Pages_comments(models.Model):
    choices = [
        (0, 'Yes'),
        (1, 'No'),
    ]
    page_id = models.ForeignKey(to=Pages, on_delete=models.CASCADE)
    pages_comment_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    comment = models.TextField()
    upvote = models.IntegerField(choices=choices, default=0)
    downvote = models.IntegerField(choices=choices, default=0)

    def __str__(self):
        return str(self.comment)


class Pages_followers(models.Model):
    id = models.IntegerField(primary_key=True)
    follower_id = models.ManyToManyField(Member, related_name='followers_pages')

    def __str__(self):
        return str(self.id)
