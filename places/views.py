from django.shortcuts import render

# Create your views here.


def homeview(request):
    return render(request, "places/home.html", {})

def register(request):
    return render(request, "places/register.html", {})