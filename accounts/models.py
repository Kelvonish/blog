from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField( max_length=100)
    description = models.CharField( max_length=500)
    image = models.ImageField( upload_to="media", height_field=None, width_field=None, max_length=None)
    created = models.DateTimeField( auto_now=False, auto_now_add=False)
    updated = models.DateTimeField( auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post  = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment =models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.comment
    