from django.db import models

# Create your models here.
class Video(models.model):
    title = models.TextField()
    day = models.TextField()
    short_description = models.TextField()
    long_description = models.TextField()