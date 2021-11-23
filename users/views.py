from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST['login_username_field']
        password = request.POST['login_password_field']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Failed to Sign in, try again..."))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})
