from django.forms import ModelForm
from .models import Blog



class Blogform(forms.ModelForm):
	date = forms.DateField()

	class Meta:
		model = Blog
		