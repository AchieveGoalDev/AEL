from os import mkdir
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields.related import ForeignKey
from pathlib import Path
from AELSite.settings import MEDIA_URL

# Create your models here.

class Course(models.Model):

    def __str__(self):
        return(self.title)

    def getTitle(self):
        return self.Course.title
    
    title = models.CharField(max_length=20, default='無名講座')
    test = models.CharField(max_length=20, default='なし')
    short_description = models.TextField(default='なし')
    long_description = models.TextField(default='なし')

class Skill(models.Model):
    def __str__(self):
        return(self.name)

    name = models.CharField(max_length=10, default='無名スキル')
    skill_description = models.TextField(default='なし')

class Category(models.Model):
    def __str__(self):
        return(self.name)

    class Meta:
        verbose_name_plural='Categories'
    
    name = models.CharField(max_length=10)
    associated_skill = models.ForeignKey(Skill, on_delete=PROTECT, null=True, blank=True)
    associated_course = models.ForeignKey(Course, on_delete=CASCADE)

class Video(models.Model):

    def __str__(self):
        return (f'Day - {self.day}: ' + self.title)

    def getThumbnailFilePath(foreignKey):
        queryObject = Course.objects.get(foreignKey)
        queryObject.video_set.all()
        myPath = Path(MEDIA_URL).joinpath(queryObject).joinpath('thumbnails')
        if not myPath.exists:
            myPath.mkdir()
        return myPath

    title = models.CharField(max_length=20)
    day = models.CharField(max_length=2)
    course = models.ForeignKey(Course, on_delete=CASCADE)
    additional_skills = models.ForeignKey(Skill, on_delete=PROTECT, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=PROTECT,  null=True)
    thumbnail = models.FileField(null=True, blank=True,)
    source = models.FileField(null=True, blank=True)
    short_description = models.TextField()
    long_description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    upload_user = models.CharField(max_length=20)