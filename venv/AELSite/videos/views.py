from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from videos import models

course = models.Course.objects.get(id=1)
videos = models.Category.objects.all()

def getContext(videoQS):
    context = {}
    for video in videoQS:
        if video.category not in context['categories']:
            context['categories'] += video.category
        context['videos'] += video

@login_required
def videos(request):
    return render(request, 'videos/videos-base.html') #Fill out dynamically

@login_required
def video(request):
    return render(request, 'videos/view-video.html') #Fill out dynamically 