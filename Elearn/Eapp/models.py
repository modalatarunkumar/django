from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	t = {
	('F','Female'),('M','Male')

	}
	y = {
	(1,'Student'),(2,'Instructor')
	}
	age = models.IntegerField(default=15)
	gender = models.CharField(choices=t,max_length=10)
	mobile = models.CharField(max_length=11)
	pfimge = models.ImageField(upload_to='profileimage/',default="pydroball.png")
	usrole = models.IntegerField(choices=y,default=1)

 
class CourseCategory(models.Model):
	ctitle = models.CharField(max_length=120)


	def __str__(self):
		return self.ctitle