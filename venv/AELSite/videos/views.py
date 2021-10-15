from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import models


@login_required
def videos(request):
    videos = models.Video.objects.all()
    categories = models.Category.objects.all()
    return render(request, 'videos/videos-base.html', {'videos': videos, 'categories':categories}) #Fill out dynamically

@login_required
def video(request):
    return render(request, 'videos/view-video.html', ) #Fill out dynamically 