from django import forms
from . import models
from pagedown.widgets import PagedownWidget
from django.contrib.auth.forms import UserChangeForm


class CreateArticle(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget)
    class Meta:
        model = models.Home
        fields = ['title', 'body', 'slug', 'thumb']


class EditPostForm(UserChangeForm):
    body = forms.CharField(widget=PagedownWidget)
    class Meta:
        model = models.Home
        fields = ['title', 'body', 'slug', 'thumb']


class DeleteNewForm(forms.ModelForm):
    class Meta:
        model = models.Home
        fields = []
