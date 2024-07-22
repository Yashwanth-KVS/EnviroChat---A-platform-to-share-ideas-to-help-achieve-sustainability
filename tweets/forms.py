# from django import forms
#
#
# class ContentUploadForm(forms.Form):
#     content = forms.CharField(
#         widget=forms.Textarea(attrs={
#             'rows': 5,
#             'placeholder': 'Enter your content here...'
#         }),
#         label='Content',
#         required=True
#     )
#     image = forms.ImageField(
#         label='Upload Image',
#         required=False
#     )
#     video = forms.FileField(
#         label='Upload Video',
#         required=False,
#         widget=forms.FileInput(attrs={
#             'accept': 'video/*'
#         })
#     )
from django import forms
from .models import MediaContent


# class ContentUploadForm(forms.ModelForm):
#     content = forms.CharField(
#         widget=forms.Textarea(attrs={
#             'rows': 5,
#             'placeholder': 'Enter your content here...'
#         }),
#         label='Content',
#         required=True
#     )
#     image = forms.ImageField(
#         label='Upload Image',
#         required=False
#     )
#     video = forms.FileField(
#         label='Upload Video',
#         required=False,
#         widget=forms.FileInput(attrs={
#             'accept': 'video/*'
#         })
#     )


class ContentUploadForm(forms.ModelForm):
    class Meta:
        model = MediaContent
        fields = ['content', 'image', 'video']
