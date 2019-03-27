from django import forms
from .models import FibonacciValue

class FibonacciForm(forms.ModelForm):
	class Meta:
		model = FibonacciValue
		exclude = ('value',)
	
