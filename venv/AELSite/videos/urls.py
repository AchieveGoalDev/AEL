from django.urls import path

from .views import videos, video

urlpatterns =[
    path('', videos, name='videos'),
    path('video/', video, name= 'video'),
]