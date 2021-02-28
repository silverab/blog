from django.shortcuts import render, Http404, redirect, HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import CreateUserForm, UserInfoForm
from .models import Blog, UserInfo
from datetime import datetime, timedelta

def home(request):
	template = 'post/index.html'
	return render(request, template)

def about(request):
	template = 'post/about_us.html'
	return render(request, template)

def services(request):
	template = 'post/services.html'
	return render(request, template)

def postblog(request):
	posts = Blog.objects.all()
	context = {'posts': posts }
	template = 'post/blog.html'
	return render(request, template, context)


def single_post(request, slug):
	post = Blog.objects.get(slug=slug)
	template = 'post/single_post.html'
	context = {'post': post }
	return render(request, template, context)


def SignUp(request):
	if request.method == 'POST':

		form = CreateUserForm(request.POST)
		info_form = UserInfoForm(request.POST, request.FILES)


		if form.is_valid() and info_form.is_valid():
			user =	form.save()
			profile = info_form.save(commit=False)
			profile.user = user
			profile.save()


			# username = form.cleaned_data.get('username')
			# password = form.cleaned_data.get('password1')
			# user = authenticate()
			login(request, user, backend='django.contrib.auth.backends.ModelBackend')

			return redirect('home')
	else:
		# cookie_name = request.COOKIES.get('name', 'Guest') ## get cookie to show in browser
		# cookie_name = request.get_singed_cokkie('name', salt='ab')
		form = CreateUserForm()
		info_form = UserInfoForm(request.POST, request.FILES)
		context = {'form': form, 'info_form': info_form}
		return render(request, 'registration/signup.html', context)
	
	# return redirect('login')