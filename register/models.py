#from django.db import models

# Create your models here.

#class User(models.Model):
#    email = models.CharField(max_length=100)
#    password = models.CharField(max_length=300)
#    activated = models.BooleanField(default=False)
#    joinDate = models.DateField(blank=True, null=True)

from mongoengine import *

connect('realtimeQuestions_DB')

class User(Document):
    _id = StringField(required=True)
    password = StringField(required=True)
    activated = BooleanField(required=True)
    joinDate = DateTimeField()

