from django.db import models

class FibonacciValue(models.Model):
    """
    Description: Stores the fibonacci value for a number
    """

    # Stores the number (nth term)
    number = models.IntegerField()

    # This stores the value for a corresponding number 
    # As the values are very very large for large numbers we use a textfield
    value = models.TextField()

    def __str__(self):
    	return str(self.number)