from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404

from .forms import PostForm
from .models import Post


def index(request):
    """The home page for Blog."""
    return render(request, 'blogs/index.html')

def posts(request):
    """Show all posts."""
    # posts = Post.objects.filter(owner=request.user).order_by('date_added')
    posts = Post.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)

@login_required
def post(request, post_id):
    """Show a single post"""
    post = Post.objects.get(id=post_id)
    # Make sure the post belongs to the current user
    check_post_owner(request, post)

    context = {'post': post}
    return render(request, 'blogs/post.html', context)

@login_required
def new_post(request):
    """Add a new post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:posts')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Edit an existing post."""
    post = Post.objects.get(id=post_id)
    check_post_owner(request, post)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = PostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=post.id)

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

def check_post_owner(request, post):
    if post.owner != request.user:
        raise Http404