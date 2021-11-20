from django.urls import path
from . import views

# url configuration

urlpatterns = [
    path('', views.homeview, name='home'),
]