from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import PetUser, Pet, PetPhoto, Interested, Message, PetAddress


admin.site.register(PetUser, UserAdmin)
admin.site.register(Pet)
admin.site.register(PetPhoto)
admin.site.register(Interested)
admin.site.register(Message)
admin.site.register(PetAddress)
