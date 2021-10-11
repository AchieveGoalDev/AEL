from django.http import HttpResponse

HTML_STRING ="""
<h1>Hello World!</h1>
"""

def index(request):
    return HttpResponse(HTML_STRING)