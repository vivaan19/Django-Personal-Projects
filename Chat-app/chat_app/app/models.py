from django.db import models
from datetime import datetime

class Room(models.Model):
    name = models.CharField(max_length=10000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=10000000)
    room = models.CharField(default="",max_length=100000)

# Create your models here.
