from django.contrib import admin
from myapp_bosun.models import Member, PagesComments, PagesFollowers, ThreadComments, Threads, Followers, Favorites, Feeds, Pages, Posts, PostComments, PostLikes

# Register your models here.
admin.site.register(Pages)
admin.site.register(PagesComments)
admin.site.register(PagesFollowers)
admin.site.register(ThreadComments)
admin.site.register(Threads)
admin.site.register(Followers)
admin.site.register(Favorites)
# admin.site.register(Member)
# admin.site.register(Feeds)
admin.site.register(Posts)
admin.site.register(PostComments)
admin.site.register(PostLikes)

@admin.register(Feeds)
class FeedsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'updated_at')  #

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'dob')


