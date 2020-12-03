from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Kharj(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    Amount = models.BigIntegerField(max_length=10)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.Amount} Tooman'

class Dakhl(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    Amount = models.BigIntegerField(max_length=10)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.Amount} Tooman'
