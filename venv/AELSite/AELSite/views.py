from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'heroContent.html')

def faq(request):
    return render(request, 'faqContent.html')

def contact(request):
    return render(request, 'contactContent.html')