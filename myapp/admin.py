from django.contrib import admin
from .models import Followers, Member

# Ensure that models are registered only once
admin.site.register(Followers)
admin.site.register(Member)
