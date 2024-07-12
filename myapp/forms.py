from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Followers, Member


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


STATIC_FOLLOWERS = [
    ('john', 'John'),
    ('jack', 'Jack'),
    ('charles', 'Charles'),
    ('david', 'David'),
    ('alex', 'Alex'),
]

STATIC_FOLLOWIE = [
    ('john', 'John'),
    ('jack', 'Jack'),
    ('charles', 'Charles'),
    ('david', 'David'),
    ('alex', 'Alex'),
]


class FollowerForm(forms.ModelForm):
    follower = forms.ChoiceField(choices=STATIC_FOLLOWERS, label="Follower")
    followee = forms.ChoiceField(choices=STATIC_FOLLOWIE, label="Followee")
    status = forms.ChoiceField(choices=[(1, 'Follower'), (2, 'Following')], label="Status")

    class Meta:
        model = Followers
        fields = ['follower', 'followee', 'status']
class SearchForm(forms.Form):
    query = forms.CharField(label='Search for a member', max_length=100)
    fields = ['username', 'email', 'password1', 'password2']

