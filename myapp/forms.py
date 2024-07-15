from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from myapp.models import Pages

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PageCreateForm(forms.Form):
        model = Pages
        title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
        title_img = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
        content_img = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
        about_page = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
        about_img = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
