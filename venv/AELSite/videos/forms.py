from django import forms
from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
            'title',
            'day',
            'short_description',
            'long_description',
        ]