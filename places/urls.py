from django.urls import path
from . import views

# url configuration

urlpatterns = [
    path('', views.home, name='home'),
    # path('register/', views.register, name='register'),
    path('profile-page/', views.profile, name='profile'),
]