from django.conf.urls import url
from rest_framework import routers
from . import views

urlpatterns = [
    url(r'^api/pet$',views.pet_list)
]