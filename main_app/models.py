from django.db import models
# Create your models here.
class Hobby(models.Model):
	"""docstring for Hobby"""
	name = models.CharField(max_length = 32, unique = True)
	image = models.ImageField(upload_to = 'logo', null = True)
	# path_logo = models.CharField(max_length = 64)
	# time_begin = models.PositiveIntegerField(blank = True, null = True)
	def __str__(self):
		return self.name
class Master(models.Model):
	"""docstring for Master"""
	name = models.CharField(max_length = 32, unique = True)
	second_name = models.CharField(max_length = 64)
	age = models.DateField(blank = True, null = True)
	def __str__(self):
		return self.name
class Organization(models.Model):
	"""docstring for Organization"""
	name = models.CharField(verbose_name = 'Название', max_length = 32)
	region = models.CharField(verbose_name = 'Регион',max_length = 32)
	tax_id = models.PositiveIntegerField(verbose_name = 'ИНН', null=True)
	site = models.CharField(verbose_name = 'Сайт',max_length = 64,blank = True, null = True)
	def __str__(self):
		return self.name
class Work(models.Model):
	organization = models.ForeignKey(Organization, verbose_name = 'Организация', null=True)
	post = models.CharField(verbose_name = 'Должность',max_length = 64)
	desc = models.TextField(verbose_name = 'Обязанности',blank = True, null = True)
	period = models.PositiveIntegerField(verbose_name = 'Время работы', default =1)
	def __str__(self):
		return self.post		
class Study(models.Model):
	"""docstring for Study"""
	name =  models.CharField(max_length = 64, unique = True)
	date_start = models.DateField(blank = True, null = True)
	date_end = models.DateField(blank = True, null = True)
	facultet = models.TextField(blank = True, null = True)
	def __str__(self):
		return self.name
# class Logo(models.Model):
# 	"""docstring for Logo"""
	
# 	def __str__(self):
# 		return self.image.url
		
