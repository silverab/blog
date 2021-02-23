from django.views.generic import ListView
from .models import Blog


class IndexPageView(ListView):
	model = Blog
	context_object_name = 'bloglist'
	queryset = Blog.objects.all()
	template_name = 'post/index.html'
