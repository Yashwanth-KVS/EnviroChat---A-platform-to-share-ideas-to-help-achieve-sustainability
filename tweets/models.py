from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone
import PIL
from django.db import models
from PIL import Image


class MediaContent(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='media_contents')
    content = models.TextField()
    image = models.ImageField(upload_to='images/%y', blank=True, null=True)
    video = models.FileField(upload_to='videos/%y', blank=True, null=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f"MediaContent {self.id}"


#


# # Create the first static entry
# MediaContent.objects.create(
#     content="This is the first test post content.",
#     image="uploads/test_image_1.jpg",  # Ensure this path matches your MEDIA_ROOT settings
#     video="uploads/test_video_1.mp4"  # Ensure this path matches your MEDIA_ROOT settings
# )
#
# # Create the second static entry
# MediaContent.objects.create(
#     content="This is the second test post content.",
#     image="uploads/test_image_2.jpg",  # Ensure this path matches your MEDIA_ROOT settings
#     video=None
# )
#
# # Create the third static entry
# MediaContent.objects.create(
#     content="This is the third test post content.",
#     image=None,
#     video="uploads/test_video_2.mp4"  # Ensure this path matches your MEDIA_ROOT settings
# )

# class Member(User):
#     user_id = models.IntegerField(unique=True, primary_key=True)
#     email_id = models.EmailField(unique=True)
#     dob = models.DateField(default=datetime.date.today)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.first_name
#
# class Followers(models.Model):
#     STATUS_CHOICES = [
#         (1, 'Request'),
#         (2, 'Following'),
#     ]
#     id = models.IntegerField(primary_key=True)
#     follower_id = models.ManyToManyField(Member, related_name='followers',STATUS_CHOICES=1)
#     followee_id = models.ManyToManyField(Member, related_name='following',STATUS_CHOICES=2)
#     request_id=models.ManyToManyField(Member,related_name='user_id')
#
#     def __str__(self):
#         return str(self.follower_id)
#
#
# class feeds(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return str(self.id)
#
#
# class Posts(models.Model):
#     STATUS_CHOICES = [
#         (1, 'Thread'),
#         (2, 'Regular Post'),
#         (3, 'Video Post'),
#     ]
#
#     id = models.IntegerField(primary_key=True)
#     user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
#     category = models.IntegerField(choices=STATUS_CHOICES, default=2)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return str(self.id)
#
# class Favorites(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
#     post_id = models.ForeignKey(to=Posts, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return str(self.id)
#
#
# class feeds_posts(models.Model):
#     id = models.IntegerField(primary_key=True)
#     post_id = models.ForeignKey(to=Posts, on_delete=models.CASCADE)
#     feed_id = models.ForeignKey(to=feeds, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return str(self.id)
