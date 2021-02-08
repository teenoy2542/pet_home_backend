from rest_framework import viewsets

from .models import PetUser , Pet , PetPhoto , Interested , Message 
from .serializers import UserSerializer , PetSerializer , PetPhotoSerializer , InterestedSerializer , MessageSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = PetUser.objects.all()
    serializer_class = UserSerializer

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PetPhotoViewSet(viewsets.ModelViewSet):
    queryset = PetPhoto.objects.all()
    serializer_class = PetPhotoSerializer

class InterestedViewSet(viewsets.ModelViewSet):
    queryset = Interested.objects.all()
    serializer_class = InterestedSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer