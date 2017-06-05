from django.db import models
class task(models.Model):
	taskname = models.CharField(max_length=50)
	taskdesciption = models.CharField(max_length=50)
	complete = models.CharField(max_length=50)

