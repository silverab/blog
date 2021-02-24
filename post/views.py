from django.shortcuts import render, Http404
from .models import Blog


def postblog(request):
	posts = Blog.objects.all()
	context = {'posts': posts }
	template = 'post/index.html'
	return render(request, template, context)


def single_post(request, slug):
	post = Blog.objects.get(slug=slug)
	template = 'post/single_post.html'
	context = {'post': post }
	return render(request, template, context)