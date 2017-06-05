from django.db import models

# Create your models here.
class task(models.Model):
	taskname = models.CharField(max_length=50)
	taskdesciption = models.CharField(max_length=50)
	complete = models.CharField(max_length=50)
	
		