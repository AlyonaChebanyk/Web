from django import forms
from .models import Comment
from django.conf import settings


class UserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)


class CommentForm(forms.Form):
    text = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'cols': '70', 'rows': '7'}))
