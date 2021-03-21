from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(label="Post Title")
    text = forms.CharField(label="Text", widget=forms.Textarea())
    class Meta:
        model = Post
        fields = ['title', 'text']
        labels = {'title': '', 'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}