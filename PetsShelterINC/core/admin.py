from django.contrib import admin
from .models import *


# Вход в админку nikita 12345
# Вход в админку nikita277 Jd9ogl0H


@admin.register(Pets)
class AdminPets(admin.ModelAdmin):
    list_display = ('pet_name', 'pet_status', 'pet_gender', 'pet_age')
    list_editable = ('pet_status', 'pet_age')
    list_filter = ('pet_status', 'pet_gender')
    search_fields = ('pet_name', 'pet_gender')


@admin.register(Contact)
class AdminPets(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_phone', 'contact_email')


# @admin.register(PetsBreed)
# class AdminPets(admin.ModelAdmin):
#     list_display = ('idpet_breed', 'breed')


@admin.register(Shelters)
class AdminPets(admin.ModelAdmin):
    list_display = ('shelter_place', 'shelter_name', 'shelter_city')


@admin.register(FoundPets)
class AdminPets(admin.ModelAdmin):
    list_display = (
        'found_pet_name', 'found_pet_status', 'found_pet_gender', 'found_pet_age', 'found_pet_found_datetime')
    list_editable = ('found_pet_status', 'found_pet_age')
    list_filter = ('found_pet_status', 'found_pet_gender', 'found_pet_found_datetime')
    search_fields = ('found_pet_name', 'found_pet_gender')


admin.site.register(LostPets)
admin.site.register(Events)
