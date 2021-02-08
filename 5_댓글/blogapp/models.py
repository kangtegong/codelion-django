from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to ='blog_photo')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment