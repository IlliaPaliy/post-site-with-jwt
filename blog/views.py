from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView
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


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title','content']
	

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

