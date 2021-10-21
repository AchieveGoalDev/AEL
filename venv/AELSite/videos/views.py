from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import models

def unpack():
    course = models.Course.objects.all()
    context_dict={}
    context_dict['categorylist'] = course[0].unpack_categories()
    context_dict['videolist'] = course[0].unpack_videos()       
    return context_dict

@login_required
def videos(request):
    context = unpack()
    return render(request, 'videos-base.html', context)

@login_required
def video(request):
    return render(request, 'view-video.html')