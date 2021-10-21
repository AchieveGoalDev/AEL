from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if  request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            context ={'error':'ユーザー名またはパスワードは違います'}
            return render(request, 'login.html', context)
        login(request, user)
        return redirect('/admin')
    return render(request, 'login.html')


def logout_view(request):
    if request.method =="POST":
        logout(request)
        return redirect('login')
    return render(request, "logout.html", {})