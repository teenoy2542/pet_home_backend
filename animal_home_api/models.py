# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.conf import settings

# class PetUser(AbstractUser):
#     phone = models.IntegerField(blank=True,null=True)
#     address = models.CharField(max_length=200,)
#     types = models.CharField(max_length=50,)
#     # photo = models.ImageField()

# class Pet(models.Model):
#     pet_id = models.IntegerField(blank=True,null=True)    
#     owner_username = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )
#     pet_type = models.CharField(max_length=10,)
#     pet_age = models.CharField(max_length=10,)
#     pet_sex = models.CharField(max_length=20,)
#     disease = models.CharField(max_length=200)
#     habit = models.CharField(max_length=250)
#     status = models.CharField(max_length=50,)
#     province = models.CharField(max_length=100,)
#     district = models.CharField(max_length=100,)

# class PetPhoto(models.Model):
#     pet_photo_id = models.IntegerField(blank=True,null=True)
#     pet_id = models.ForeignKey(Pet,on_delete=models.CASCADE)
#     # pet_photo = models.ImageField()

# class Interested(models.Model):
#     pet_id = models.ForeignKey(Pet,on_delete=models.CASCADE)
#     username = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     ) 

# class Message(models.Model):
#     messsage_id = models.IntegerField(blank=True,null=True)
#     pet_id = models.ForeignKey(Pet,on_delete=models.CASCADE)
#     username = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )
#     message = models.CharField(max_length=300,)
#     message_date = models.DateField()
#     message_time = models.TimeField()