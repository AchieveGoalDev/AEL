from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Course(models.Model):

    def __str__(self):
        return(self.title)
    
    title = models.CharField(max_length=20, default='無名講座')
    test = models.CharField(max_length=20, default='なし')
    short_description = models.TextField(default='なし')
    long_description = models.TextField(default='なし')

class Skill(models.Model):
    def __str__(self):
        return(self.name)

    name = models.CharField(max_length=10, default='無名スキル')
    skill_description = models.TextField(default='なし')

class Video(models.Model):

    def __str__(self):
        return (f'Day - {self.day}: ' + self.title)

    title = models.CharField(max_length=20,)
    day = models.CharField(max_length=2)
    course = models.ForeignKey(Course, on_delete=CASCADE, default=0)
    skill = ForeignKey(Skill, on_delete=PROTECT, default=0)
    short_description = models.TextField()
    long_description = models.TextField()
