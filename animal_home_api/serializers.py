from .models import PetUser , Pet , PetPhoto , Interested , Message 
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PetUser
        fields = ('id', 'username' , 'password' ,'first_name' , 'last_name'  , 'email' , 'phone' , 'address' )

class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

class PetPhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PetPhoto
        fields = '__all__'

class InterestedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interested
        fields = '__all__'

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = '__all__' 