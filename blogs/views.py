from django.shortcuts import render

from .models import Post

def index(request):
    """The home page for Blog."""
    return render(request, 'blogs/index.html')

def posts(request):
    """Show all topics."""
    posts = Post.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)