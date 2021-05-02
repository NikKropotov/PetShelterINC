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
    list_display = ('contact_mane', 'contact_phone', 'contact_email')
