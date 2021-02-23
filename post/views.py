from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog


def postblog(request):
	posts = Blog.objects.all()
	context = {'posts': posts }
	template = 'post/index.html'
	return render(request, template, context)

# class IndexPageView(ListView):
# 	model = Blog
# 	context_object_name = 'bloglist'
# 	queryset = Blog.objects.all()
# 	template_name = 'post/index.html'
