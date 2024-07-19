from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ipywidgets import Video
from .models import video


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = video
        fields = ['Title', 'video']