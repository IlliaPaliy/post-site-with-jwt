from django.contrib import admin
from . import views
from django.urls import path, include
from .views import PostListView


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', PostListView.as_view(), name='home'),

    ]


