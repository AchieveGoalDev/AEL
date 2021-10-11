from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render

templ= render_to_string("baseunl.html")

def index(request):
    return HttpResponse(templ)

