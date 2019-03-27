from rest_framework import serializers

from .models import FibonacciValue

class FibonacciSerializer(serializers.ModelSerializer):
	class Meta:
		model = FibonacciValue
		fields = 'number'