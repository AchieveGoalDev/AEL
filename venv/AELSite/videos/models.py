from os import mkdir
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields.related import ForeignKey
from django.conf import settings
from pathlib import Path

# Create your models here.

class Skill(models.Model):
    def __str__(self):
        return(self.name)

    name = models.CharField(max_length=10, default='無名スキル')
    skill_description = models.TextField(default='なし')

class Test(models.Model):
    def __str__(self):
        return(self.name)
    
    name = models.CharField(max_length=20)
    skills_tested = models.ManyToManyField(Skill)

class Video(models.Model):

    def __str__(self):
        return (f'Day - {self.day}: ' + self.title)

    title = models.CharField(max_length=20)
    day = models.CharField(max_length=2)
    additional_skills = models.ManyToManyField(Skill, blank=True)
    thumbnail = models.FileField(null=True, blank=True,)
    source = models.FileField(null=True, blank=True)
    short_description = models.TextField()
    long_description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    upload_user = models.CharField(max_length=20)

class Category(models.Model):
    def __str__(self):
        return(self.name)

    class Meta:
        verbose_name_plural='Categories'
    
    name = models.CharField(max_length=10)
    order = models.IntegerField(null=True, blank=True)
    videos = models.ManyToManyField(Video)
    associated_skill = models.ForeignKey(Skill, on_delete=PROTECT, null=True, blank=True)

class Course(models.Model):

    def __str__(self):
        return(self.title)

    def getTitle(self):
        return self.Course.title
    
    title = models.CharField(max_length=20, default='無名講座')
    test = models.CharField(max_length=20, default='なし')
    categories = models.ManyToManyField(Category)
    short_description = models.TextField(default='なし')
    long_description = models.TextField(default='なし')