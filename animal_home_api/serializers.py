from rest_framework import serializers
from .models import PetUser, Pet, PetPhoto, Interested, Message, PetAddress


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetUser
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'phone', 'address', 'photo')


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'


class PetAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetAddress
        fields = '__all__'


class PetPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetPhoto
        fields = '__all__'


class InterestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interested
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
