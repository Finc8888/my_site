from django.db import models

# Create your models here.
class Work(models.Model):
	name = models.CharField(max_length = 32, unique = True)
	post = models.CharField(max_length = 64)
	desc = models.TextField(blank = True, null = True)
	def __str__(self):
		return self.name
class Hobby(models.Model):
	"""docstring for ClassName"""
	name = models.CharField(max_length = 32, unique = True)
	# path_logo = models.CharField(max_length = 64)
	# time_begin = models.PositiveIntegerField(blank = True, null = True)
	def __str__(self):
		return self.name
class Master(models.Model):
	"""docstring for ClassName"""
	name = models.CharField(max_length = 32, unique = True)
	second_name = models.CharField(max_length = 64)
	age = models.DateField(blank = True, null = True)
	def __str__(self):
		return self.name
class Organization(models.Model):
	"""docstring for Organization"""
	name = models.CharField(max_length = 32, unique = True)
	region = models.CharField(max_length = 32)
	tax_id = models.PositiveIntegerField(blank = True, null = True)
	site = models.CharField(max_length = 32)
	def __str__(self):
		return self.name
class Study(models.Model):
	"""docstring for Study"""
	name =  models.CharField(max_length = 64, unique = True)
	date_start = models.DateField(blank = True, null = True)
	date_end = models.DateField(blank = True, null = True)
	facultet = models.TextField(blank = True, null = True)
	def __str__(self):
		return self.name
		
