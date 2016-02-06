from __future__ import unicode_literals

from django.db import models

# Create your models here.

class GuaziCar(models.Model):
	name = models.CharField(max_length=512)
	city = models.CharField(max_length=512)
	time = models.CharField(max_length=512)
	mile = models.CharField(max_length=512)
	price = models.CharField(max_length=512)