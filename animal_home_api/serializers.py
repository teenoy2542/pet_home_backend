from rest_framework import serializers
from .models import PetUser, Pet, PetPhoto, Interested, Message, PetAddress
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetUser
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'phone_number', 'address', 'photo_user')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetUser
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'phone_number', 'address', 'photo_user')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = PetUser.objects.create_user(
            username = validated_data['username'], 
            password = validated_data['password'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            phone_number = validated_data['phone_number'],
            address = validated_data['address'],
            photo_user = validated_data['photo_user']
             )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)       
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


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
