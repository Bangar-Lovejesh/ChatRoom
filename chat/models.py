from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100)

class Messages(models.Model):
    message = models.CharField(max_length=10000000)
    date = models.DateTimeField(default=datetime.now, blank = True)
    user = models.CharField(max_length=1000)
    roomName = models.CharField(max_length = 10000000)