from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField()
    day = models.CharField()
    short_description = models.TextField()
    long_description = models.TextField()

