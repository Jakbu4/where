from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from users.views import user_login
from .models import Place
# Create your views here.


def home(request):
    user_selection = request.POST.get('user_select')
    if user_selection is not None:
        places = Place.objects.all().order_by('-'+user_selection)
    else:
        places = Place.objects.all()
    return render(request, "places/home.html", {'places': places})


def profile(request):
    places = Place.objects.filter(author = request.user)
    return render(request, "places/profile-page.html", {'places': places})


def edit_profile(request):
    return render(request, "places/edit-profile.html", {})


def create_place(request):
    return render(request, "places/create-place.html", {})


def add_place(request):
    place_title = request.POST.get('place_name')
    place_type = request.POST.get('place_type')
    place_city = request.POST.get('place_location')
    place_address = request.POST.get('place_address')
    place_description = request.POST.get('place_desc')
    place_image = request.FILES['place_photo']
    place_author = request.user

    place_info = Place(title=place_title, type=place_type,
                        city=place_city, address=place_address,
                        description=place_description, image=place_image,
                        author=place_author)
    place_info.save()

    print(place_image)

    return redirect('profile')


def delete_place(request, place_id):
    place = Place.objects.get(pk=place_id)
    place.delete()
    return redirect('profile')