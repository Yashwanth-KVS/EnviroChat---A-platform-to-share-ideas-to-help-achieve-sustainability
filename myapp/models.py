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


class Posts(models.Model):
    STATUS_CHOICES = [
        (1, 'Thread'),
        (2, 'Regular Post'),
        (3, 'Video Post'),
    ]

    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    category = models.IntegerField(choices=STATUS_CHOICES, default=2)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class Favorites(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    post_id = models.ForeignKey(to=Posts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class feeds_posts(models.Model):
    id = models.IntegerField(primary_key=True)
    post_id = models.ForeignKey(to=Posts, on_delete=models.CASCADE)
    feed_id = models.ForeignKey(to=feeds, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
