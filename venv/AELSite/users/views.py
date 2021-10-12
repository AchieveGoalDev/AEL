from django.shortcuts import render
from django.contrib.auth import authenticate, login

def login_view(request):
    if  request.method == "POST":
        username = request.post.get("username")
        password = request.post.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            pass
    return render(request, "accounts/login.html", {})

def logout_view(request):
    return render(request, "accounts/logout.html", {})

def register_view(request):
    return render(request, "accounts/register.html")