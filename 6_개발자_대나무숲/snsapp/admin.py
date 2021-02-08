from django.contrib import admin
from .models import Post, Comment, FreePost, FreeComment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(FreePost)
admin.site.register(FreeComment)
