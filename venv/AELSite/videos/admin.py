from django.contrib import admin

from .models import Video, Course, Skill, Category, Test

class TestAdmin(admin.ModelAdmin):
    filter_horizontal= ('skills_tested',)

class CourseAdmin(admin.ModelAdmin):
    filter_horizontal =('skills_taught',)

class VideoAdmin(admin.ModelAdmin):
    filter_horizontal = ('additional_skills',)

class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal = ('videos',)
admin.site.register(Video, VideoAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Skill)
admin.site.register(Category)
admin.site.register(Test)