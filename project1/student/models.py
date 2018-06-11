from django.db import models
from django.utils import timezone

class student(models.Model):
	author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	studID = models.CharField(max_length=100)
	studFName = models.CharField(max_length=100)
	studLname = models.CharField(max_length=100)
	studAddress = models.CharField(max_length=100)

	def __str__(self):
		name = self.studFName + " " + self.studLname
		return name 




# Create your models here.
