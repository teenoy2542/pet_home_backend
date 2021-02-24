from rest_framework import generics, permissions, serializers
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from django.contrib.auth import login


from .models import PetUser, Pet, PetPhoto, Interested, Message
from .serializers import LoginSerializer, UserSerializer, PetSerializer, PetPhotoSerializer, InterestedSerializer, MessageSerializer, RegisterSerializer


class RegisterAPI(generics.GenericAPIView):    
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)        
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data       
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

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





