from django.db import models

# Create your models here.

class User(models.Model):
    _id = models.CharField(max_length=100)
    password = models.CharField(max_length=300)

