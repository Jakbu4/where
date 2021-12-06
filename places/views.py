from django.shortcuts import render
from .models import Place
# Create your views here.


def home(request):
    places = Place.objects.all()
    return render(request, "places/home.html", {'places': places})


def profile(request):
    return render(request, "places/profile-page.html", {})


def edit_profile(request):
    return render(request, "places/edit-profile.html", {})


def create_place(request):
    return render(request, "places/create-place.html", {})
