from django.contrib import admin
from . import views
from django.urls import path, include
from .views import PostListView, PostCreateView


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', PostListView.as_view(), name='home'),
    path('post/new/', PostCreateView.as_view(), name='create_post')
    ]


