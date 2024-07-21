from random import choices

from django.db import models
import datetime
from django.contrib.auth.models import User



class Member(User):
    user_id = models.AutoField(unique=True, primary_key=True)
    email_id = models.EmailField(unique=True)
    dob = models.DateField(default=datetime.date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='profile_pictures')
    cover_picture = models.ImageField(upload_to='cover_pictures')
    interests = models.TextField(blank=True)

    def __str__(self):
        return str(self.user_id)


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