from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from myapp.models import Pages, Video, MediaContent, Member


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Member
        fields = ['username', 'first_name', 'last_name', 'email', 'password1']


class PageCreateForm(forms.ModelForm):
        class Meta:
            model = Pages
            fields = ['title', 'content', 'title_img', 'content_img', 'about_img', 'about_page']
            # title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
            # content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
            # title_img = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
            # content_img = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
            # about_page = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
            # about_img = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))


class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['Title', 'video']
        ##labels = {'Title': 'Title', 'video': 'Video'}

class ContentUploadForm(forms.ModelForm):
    class Meta:
        model = MediaContent
        fields = ['content', 'image', 'video']