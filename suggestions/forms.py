from django import forms
from .models import *

class suggestionform(forms.ModelForm):
	class Meta:
		model = suggestion
		fields = ['contact', 'transport', 'field', 'site']
