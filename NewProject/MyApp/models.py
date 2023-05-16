from django.db import models

# Create your models here.
class Sregister(models.Model):
	sname = models.CharField(max_length=100)
	age = models.IntegerField()
	suname = models.CharField(max_length=100)
	spwd = models.CharField(max_length=100)
	semail = models.EmailField(max_length=100)
