import datetime
from django.db import models
from django.utils import timezone


# Create your models here.

class Results(models.Model):
    date = models.DateTimeField('date of scrape')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
