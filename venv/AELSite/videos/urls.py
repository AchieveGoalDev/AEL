from django.urls import path

from .views import videos, video, courses, tests

urlpatterns =[
    path('', videos, name='videos'),
    path('video/', video, name= 'video'),
    path('courses/', courses, name ='courses'),
    path('tests/', tests, name='tests')
]