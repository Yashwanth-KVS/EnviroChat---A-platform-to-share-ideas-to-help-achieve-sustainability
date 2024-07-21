from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone

class Member(User):
    user_id = models.AutoField(unique=True, primary_key=True)
    email_id = models.EmailField(unique=True)
    dob = models.DateField(default=datetime.date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    cover_picture = models.ImageField(upload_to='cover_pictures', blank=True, null=True)
    interests = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Members'

    def __str__(self):
        return self.username

class Followers(models.Model):
    STATUS_CHOICES = [
        (1, 'Request'),
        (2, 'Following'),
    ]
    follower_id = models.ManyToManyField(Member, related_name='followers', blank=True)
    followee_id = models.ManyToManyField(Member, related_name='following', blank=True)
    requests = models.ManyToManyField(Member, related_name='requests_received', blank=True)

    class Meta:
        verbose_name_plural = 'Followers'

    def __str__(self):
        return str(self.id)

class Feeds(models.Model):
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(default=timezone.now)
    threads = models.ManyToManyField('Threads', related_name='feeds_threads', blank=True)
    pages = models.ManyToManyField('Pages', related_name='feeds_pages', blank=True)
    posts = models.ManyToManyField('Posts', related_name='feeds_posts', blank=True)

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

class Pages(models.Model):
    page_id = models.AutoField(primary_key=True)
    feed = models.ForeignKey(Feeds, on_delete=models.CASCADE, related_name='pages_related', default=1)  # Added default value
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Pages'

    def __str__(self):
        return str(self.title)

class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    feed = models.ForeignKey(Feeds, on_delete=models.CASCADE, related_name='posts_related', default=1)  # Added default value
    user_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_images', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return str(self.post_id)

class ThreadComments(models.Model):
    thread_comment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    thread_id = models.ForeignKey(to=Threads, on_delete=models.CASCADE)
    comment = models.TextField()
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    feed = models.ForeignKey(Feeds, on_delete=models.CASCADE, related_name='threads_comments', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ThreadComments'

    def __str__(self):
        return str(self.comment)

class Favorites(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    thread_id = models.ForeignKey(to=Threads, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Favourites'

    def __str__(self):
        return str(self.id)

class PagesComments(models.Model):
    page_comment_id = models.AutoField(primary_key=True)
    page_id = models.ForeignKey(to=Pages, on_delete=models.CASCADE)
    user_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    comment = models.TextField()
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    feed = models.ForeignKey(Feeds, on_delete=models.CASCADE, related_name='pages_comments', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Pages_comments'

    def __str__(self):
        return str(self.comment)

class PagesFollowers(models.Model):
    id = models.AutoField(primary_key=True)
    page_id = models.ForeignKey(to=Pages, on_delete=models.CASCADE)
    follower_id = models.ForeignKey(to=Member, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Pages_followers'

    def __str__(self):
        return str(self.id)

class PostComments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    user_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    feed = models.ForeignKey(Feeds, on_delete=models.CASCADE, related_name='posts_comments', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'PostComments'

    def __str__(self):
        return str(self.comment_id)

class PostLikes(models.Model):
    like_id = models.AutoField(primary_key=True)
    feed = models.ForeignKey(Feeds, on_delete=models.CASCADE, default=1)  # Added default value
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='likes')
    user_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'PostLikes'

    def __str__(self):
        return f'Post {self.post_id} liked by {self.user_id}'
