from django.db import models
from datetime import datetime

class blog_model(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    blog_title = models.CharField(max_length=100, default="", editable=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
# Create your models here.
