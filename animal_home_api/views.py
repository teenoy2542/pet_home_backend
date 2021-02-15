from rest_framework import generics

from .models import PetUser, Pet, PetPhoto, Interested, Message
from .serializers import UserSerializer, PetSerializer, PetPhotoSerializer, InterestedSerializer, MessageSerializer


class UserCreate(generics.CreateAPIView):
    queryset = PetUser.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PetUser.objects.all()
    lookup_field = 'id'
    serializer_class = UserSerializer


class PetView(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    lookup_field = 'pet_id'
    serializer_class = PetSerializer





