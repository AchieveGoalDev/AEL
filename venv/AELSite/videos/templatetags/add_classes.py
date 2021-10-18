from django import template
from videos.models import *

register = template.Library()

@register.filter(name = "get_videos")
def get_videos(value, arg):
    pass