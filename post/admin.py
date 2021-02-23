from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
	search_fields = ['title', 'description']
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)

