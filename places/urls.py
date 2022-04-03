from django.urls import path
from . import views

# url configuration

urlpatterns = [
    path('', views.home, name='home'),
    path('more-button/',views.more_button, name='more_button'),
    path('profile-page/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('create-place/', views.create_place, name='create_place'),
    path('add-place/', views.add_place, name='add_place'),
    path('delete-place/<place_id>', views.delete_place, name='delete_place'),
]