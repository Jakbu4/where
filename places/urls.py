from django.urls import path
from . import views

# url configuration

urlpatterns = [
    path('', views.home, name='home'),
    path('profile-page/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('create-place/', views.create_place, name='create_place'),
]