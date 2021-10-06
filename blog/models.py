from django.db import models
from django.utils import timezone
from users.models import User
from django.shortcuts import render, redirect

class Post(models.Model):
	title = models.CharField(max_length=64)
	content = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	
	class Meta:
		ordering = ['-date_posted']	
	
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return ('/home')