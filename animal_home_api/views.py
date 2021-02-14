from django.shortcuts import render

from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import PetUser, Pet, PetPhoto, Interested, Message
from .serializers import UserSerializer, PetSerializer, PetPhotoSerializer, InterestedSerializer, MessageSerializer


@api_view(['GET', 'POST', 'DELETE'])
def pet_list(request):
    if request.method == 'GET':
        pet = Pet.objects.all()
        pet_type = request.GET.get('pet_type', None)
        if pet_type is not None:
            pet = Pet.filter(pet_type__icontains=pet_type)

        pet_serializer = PetSerializer(pet, many=True)
        return JsonResponse(pet_serializer.data, safe=False)
    elif request.method == 'POST':
        pet_data = JSONParser().parse(request)
        pet_serializer = PetSerializer(data=pet_data)
        if pet_serializer.is_valid():
            pet_serializer.save()
            return JsonResponse(pet_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(pet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)