from django.shortcuts import render

def landing(request):
    return render(request, 'landing.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html') 