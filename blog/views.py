from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from users.models import User
from .models import Post

def home(request):
	return render(request, 'blog/home.html')

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'


	def get_queryset(self):
		return Post.objects.all()