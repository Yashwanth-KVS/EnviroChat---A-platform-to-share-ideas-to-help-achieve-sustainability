from django.contrib import admin
from .models import Pages, Pages_followers, Pages_comments,Member, Followers,Feeds, Posts, Favorites, FeedsPosts

# Register your models here.
admin.site.register(Pages)
admin.site.register(Pages_followers)
admin.site.register(Pages_comments)
admin.site.register(Member)
admin.site.register(Followers)
admin.site.register(Feeds)
admin.site.register(Posts)
admin.site.register(Favorites)
admin.site.register(FeedsPosts)
