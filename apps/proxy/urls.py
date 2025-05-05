from django.urls import path

from apps.proxy.views import ProxyListView, ProxyRetrieveView


class Proxy:
    endpoints = [
        path('posts/', ProxyListView.as_view(), name='proxy-list'),
        path('posts/<int:pk>/', ProxyRetrieveView.as_view(), name='proxy-retrieve'),
    ]
