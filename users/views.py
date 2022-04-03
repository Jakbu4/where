from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

def user_login(request):
    if request.method == 'POST':
        username = request.POST['login_username_field']
        password = request.POST['login_password_field']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, (f"You are logged in as {username}"))
            return redirect('home')
        else:
            messages.success(request, ("Failed to Sign in, try again..."))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def user_logout(request):
    logout(request)
    messages.success(request, ("You were logged out..."))
    return redirect('home')


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registered succesfully..."))
            return redirect('home')
    else:
        form = UserRegistrationForm()

    return render(request, "authenticate/register.html", {'form':form,})

