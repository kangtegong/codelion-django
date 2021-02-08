from django import forms
from .models import Blog, Comment

class BlogForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ['title', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        # fields = ['title', 'body']
