from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "places/home.html", {})

# def register(request):
#     return render(request, "places/register.html", {})

def profile(request):
    return render(request, "places/profile-page.html", {})
