from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class PetUser(AbstractUser):
    USER_TYPE = (
        ('ow','owner'),
        ('fi','finder'),
        )
    phone_number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=200, )
    user_type = models.CharField(max_length=50,choices=USER_TYPE)
    photo_user = models.ImageField(upload_to='images/user/', null=True)


class Pet(models.Model):
    pet_id = models.AutoField(blank=True, primary_key=True)
    owner_username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    pet_type = models.CharField(max_length=10, )
    pet_age = models.CharField(max_length=10, )
    pet_sex = models.CharField(max_length=20, )
    disease = models.CharField(max_length=200)
    habit = models.CharField(max_length=250)
    status = models.CharField(max_length=50, )


class PetAddress(models.Model):
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE)
    province = models.CharField(max_length=100, )
    district = models.CharField(max_length=100, )


class PetPhoto(models.Model):
    pet_photo_id = models.AutoField(blank=True, primary_key=True)
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE)
    pet_photo = models.ImageField(upload_to='images/pets/', null=True)


class Interested(models.Model):
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE)
    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class Message(models.Model):
    messsage_id = models.AutoField(blank=True, primary_key=True)
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE)
    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    message = models.CharField(max_length=300, )
    message_date = models.DateField()
    message_time = models.TimeField()
