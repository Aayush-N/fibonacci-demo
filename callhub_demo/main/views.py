from django.views.generic import FormView, TemplateView

import time 

from .forms import FibonacciForm
from .models import FibonacciValue

class FibonacciEntryView(FormView):
	template_name = 'entry.html'
	form_class = FibonacciForm
	success_url = '/display/'

	def fibonacci_calculation(self, number): 
		# We use matrix method as it is comparatively faster to other methods. Runtime - O(log(n))
		if number == 0: 
			return 0

		if number == 1: 
			return 1

		def matmul(M1, M2):
			a11 = M1[0][0]*M2[0][0] + M1[0][1]*M2[1][0]
			a12 = M1[0][0]*M2[0][1] + M1[0][1]*M2[1][1]
			a21 = M1[1][0]*M2[0][0] + M1[1][1]*M2[1][0]
			a22 = M1[1][0]*M2[0][1] + M1[1][1]*M2[1][1]
			return [[a11, a12], [a21, a22]]

		def matPower(mat, p):
			if p == 1: 
				return mat

			m2 = matPower(mat, p//2)
			if p % 2 == 0:
				return matmul(m2, m2)
			else: 
				return matmul(matmul(m2, m2),mat)

		Q = [[1,1],[1,0]]

		q_final = matPower(Q, number-1)
		return q_final[0][0]

	def get_context_data(self, *args, **kwargs):
		context = super(FibonacciEntryView, self).get_context_data(*args, **kwargs)
		return context

	def form_valid(self, form):
		# Get the number from the form submitted by the user
		number = form.cleaned_data['number']

		# Start calculating the time
		start_time = time.time()

		'''
		The below try/except block checks whether the value for the input number
		exists in the database. If it does, we use the same or else we compute the 
		value and store it in the database for future use.

		This will reduce the time taken significantly.
		'''
		try:
			data = FibonacciValue.objects.filter(number=number)
			value = data[0].value
		except:
			value = self.fibonacci_calculation(number)
			print(value)
			form.instance.value = value
			create = form.save()

		# Store value as a session variable
		self.request.session['value'] = value

		end_time = time.time()
		total_time = end_time - start_time

		# Store time as a session variable
		self.request.session['time'] = total_time
		return super().form_valid(form)


class DisplayFibonacciView(TemplateView):
	template_name = "display.html"

	def get_context_data(self, **kwargs):
		context = super(DisplayFibonacciView, self).get_context_data(**kwargs)

		# Get value from session
		context['value'] = self.request.session['value']

		# Get time taken to compute from session
		context['time'] = self.request.session['time']
		return context