from django.http import HttpResponse
from django.template.loader import render_to_string

templ= render_to_string("baseunl.html")
test = '<h1>Test</h1>'

def index(request):
    return HttpResponse(templ)

