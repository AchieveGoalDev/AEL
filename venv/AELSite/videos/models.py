from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=20)
    day = models.CharField(max_length=2)
    short_description = models.TextField()
    long_description = models.TextField()

