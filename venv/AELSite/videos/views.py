from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import models

def unpack():
    course = models.Course.objects.all()
    context_dict={}
    context_dict['categorylist'] = course[0].unpack_categories()
    context_dict['videolist'] = course[0].unpack_videos()
    # for item in context_dict['videolist']:
    #     if item.title in context_dict['courselist']:
    #         context_dict[item.course.name] += [item.title]        
    return context_dict

@login_required
def videos(request):
    context = unpack()
    return render(request, 'videos/videos-base.html', context) #Fill out dynamically

@login_required
def video(request):
    return render(request, 'videos/view-video.html', ) #Fill out dynamically 