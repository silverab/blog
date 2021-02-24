from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Blog(models.Model):
	id = models.IntegerField(primary_key=True, editable=False)
	admin = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	posted_date = models.DateField(blank=True, null=True)
	feature_image = models.ImageField(null=True, blank=True)
	blog_image = models.ImageField(null=True, blank=True)
	slug = models.SlugField(unique=True)
	description = models.TextField(null=True, blank=True)


	def __str__(self):
		return str(self.title) + ' | ' + str(self.admin)

	class Meta:
		unique_together = ('title', 'slug')
		ordering = ['-posted_date']

	def get_absolute_url(self):
		return reverse("single_post", kwargs={"slug":self.slug})