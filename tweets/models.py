from django.db import models

# Create your models here.
from django.shortcuts import render
# tweets/models.py
from django.contrib.auth.models import User
from django.db import models


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
