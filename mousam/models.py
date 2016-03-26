from django.db import models

# Create your models here.
class Temperature(models.Model):
	real = models.CharField(max_length = 100)
	feel = models.CharField(max_length = 100)

	def __str__(self):
		return self.real