from django.conf.urls import url
from django.urls import path
from animal_home_api.views import PetView, PetDetailView, UserDetailView, UserCreate

from rest_framework import routers
from . import views

urlpatterns = [
    path('api/user/create', UserCreate.as_view()),
    path('api/user/<int:id>', UserDetailView.as_view()),
    path('api/pet', PetView.as_view()),
    path('api/pet/<int:pet_id>', PetDetailView.as_view()),
]
