from django.db import models

# Create your models here.
class Student_Info(models.Model):
	FIRSTNAME = models.CharField(max_length=50)
	LASTNAME = models.CharField(max_length=50)
	CLGNAME = models.CharField(max_length=50)
	BRANCH = models.CharField(max_length=50)
	DOB = models.DateField()
	GENDER = models.CharField(max_length=50)
	DEPT = models.CharField(max_length=50)
	STUDENT_ID = models.CharField(max_length=50)



class Movies(models.Model):
	Name = models.CharField(max_length=100)
	Actor = models.CharField(max_length=20)
	Actress = models.CharField(max_length=20)
	Budget = models.IntegerField()

