from django.contrib import admin
from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),

    ]


