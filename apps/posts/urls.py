from django.urls import path

from apps.posts.views import PostListCreateView, PostRetrieveUpdateDestroyView


class Posts:
    endpoints = [
        path('', PostListCreateView.as_view(), name='posts-list-create'),
        path('<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='posts-retrieve-update-destroy'),
    ]
