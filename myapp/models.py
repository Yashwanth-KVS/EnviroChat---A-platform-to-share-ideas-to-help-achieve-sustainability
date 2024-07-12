from django.db import models
import datetime
from django.contrib.auth.models import User


class Member(User):
    user_id = models.AutoField(unique=True, primary_key=True)
    email_id = models.EmailField(unique=True)
    dob = models.DateField(default=datetime.date.today)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Followers(models.Model):
    STATUS_CHOICES = [
        (1, 'Request'),
        (2, 'Following'),
    ]
    id = models.AutoField(primary_key=True)
    follower = models.ForeignKey(Member, related_name='followers', on_delete=models.CASCADE)
    followee = models.ForeignKey(Member, related_name='following', on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES)

    def __str__(self):
        return f'Follower: {self.follower.username}, Followee: {self.followee.username}'


class Feeds(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


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

    def __str__(self):
        return str(self.id)


class Favorites(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class FeedsPosts(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feeds, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
