from django.contrib import admin
from .models import PetUser, Pet, PetPhoto, Interested, Message

class PetUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(PetUser, PetUserAdmin)
admin.site.register(Pet)
admin.site.register(PetPhoto)
admin.site.register(Interested)
admin.site.register(Message)