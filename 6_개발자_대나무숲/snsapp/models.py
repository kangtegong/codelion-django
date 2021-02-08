from django.db import models
from django.conf import settings 
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class FreePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class FreeComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(FreePost, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment