from django.db import models

class contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    desc = models.TextField()
    date = models.DateField()

# Create your models here.
