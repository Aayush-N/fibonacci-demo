from rest_framework.response import Response
from rest_framework.views import APIView

import time

from rest_framework.status import (
	HTTP_200_OK,
)

from .models import FibonacciValue


class FibonacciAPIView(APIView):
	"""API View to calculate fibonacci value of Nth term
		```
		atributes:
			number = This is the Nth term for which we wish to calculate the Fibonacci value
		```
		Example POST data:
			{"number": "21"}
	"""

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

	def post(self, request, *args, **kwargs):
		print(request.data)
		number = int(request.data['number'])
		start_time = time.time()
		try:
			data = FibonacciValue.objects.filter(number=number)
			value = data[0].value
		except:
			value = self.fibonacci_calculation(number)
			create = FibonacciValue.objects.create(number=number,value=value)
		end_time = time.time()
		total_time = end_time - start_time

		return Response({"value":value, "time":total_time}, status=HTTP_200_OK)

		