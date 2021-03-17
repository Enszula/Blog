"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Page that shows all posts.
    path('posts/', views.posts, name='posts'),

    # Detail page for a single topic.
    path('posts/<int:post_id>', views.post, name='post'),

    # Page for adding a new topic
    path('new_post/', views.new_post, name='new_post'),

    # Page for editing an entry.
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
]
