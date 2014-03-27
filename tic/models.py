from django.db import models

# Create your models here.
class Board(models.Model):
	zero=models.CharField(max_length=1,default='')
	one=models.CharField(max_length=1,default='')
	two=models.CharField(max_length=1,default='')
	three=models.CharField(max_length=1,default='')
	four=models.CharField(max_length=1,default='')
	five=models.CharField(max_length=1,default='')
	six=models.CharField(max_length=1,default='')
	seven=models.CharField(max_length=1,default='')
	eight=models.CharField(max_length=1,default='')
    
	def __unicode__(self):
		return self.id
