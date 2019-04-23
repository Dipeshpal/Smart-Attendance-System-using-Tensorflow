from django.db import models
from django.contrib.auth.models import User
import random
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default=random.randint(1, 1010))
    body = models.TextField()
    link = models.URLField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100]+'...'
