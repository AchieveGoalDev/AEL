from django.contrib import admin
from django.urls import path, include

from .views import index, contact
from users.views import login_view, logout_view
from videos.views import videos, video
from faq.views import faq

urlpatterns = [
    path('', login_view, name='login'),
    path('info/',include('info.urls'), name='info'),
    path('admin/', admin.site.urls, name="admin"),
    path('faq/', faq, name="faq"),
    path('logout/', logout_view, name='logout'),
    path('videos/', videos, name='videos'),
    path('video/', video, name='video')
]