from django.db import models

class student(models.Model):
	cName = models.CharField(max_length=20, null=False)
	cSex = models.CharField(max_length=2, default='M', null=False)
	cBirthday = models.DateField(null=False)
	cEmail = models.EmailField(max_length=100, blank=True, default='')
	cPhone = models.CharField(max_length=50, blank=True, default='')
	cAddr = models.CharField(max_length=255,blank=True, default='')
	
	def __str__(self):
		return self.cName

class student2(models.Model):
	no = models.CharField(max_length=50)
	companyid = models.CharField(max_length=50)
	num = models.CharField(max_length=50)
	jobname = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	company = models.CharField(max_length=50)
	cash = models.CharField(max_length=50)
	
	def __str__(self):
		return self.companyid
