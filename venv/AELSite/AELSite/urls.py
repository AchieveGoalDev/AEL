from django.contrib import admin
from django.urls import path, include

from users.views import login_view
from videos.views import videos, video

urlpatterns = [
    path('', login_view, name='login'),
    path('info/',include('info.urls'), name='info'),
    path('users/', include('users.urls'), name='users'),
    path('videos/', include('videos.urls'), name='videos'),
    path('admin/', admin.site.urls, name="admin"),
    path('videos/', videos, name='videos'),
    path('video/', video, name='video')
]