from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Total(models.Model):
	sample = models.CharField(max_length=200)
	confirmed = models.CharField(max_length=200)
	active = models.CharField(max_length=200)
	discharged = models.CharField(max_length=200)
	death = models.CharField(max_length=200)

	def __str__(self):
		return self.confirmed