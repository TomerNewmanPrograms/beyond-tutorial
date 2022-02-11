from django.db import models
from django.utils import timezone
# Create your models here.  task 3 part 5 change:


class Message(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
