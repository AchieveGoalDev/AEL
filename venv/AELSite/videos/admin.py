from django.contrib import admin

# Register your models here.
from .models import Video, Course, Skill, Category

admin.site.register(Video)
admin.site.register(Course)
admin.site.register(Skill)
admin.site.register(Category)