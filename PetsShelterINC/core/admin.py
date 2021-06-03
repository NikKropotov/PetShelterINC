from django.contrib import admin
from .models import *


# Вход в админку nikita 12345
# Вход в админку nikita277 Jd9ogl0H

@admin.register(Pets)
class AdminPets(admin.ModelAdmin):
    exclude = ('pet_toilet',)
    list_display = ('pet_name', 'pet_status', 'pet_gender', 'pet_age')
    list_editable = ('pet_status', 'pet_age')
    list_filter = ('pet_status', 'pet_gender')
    search_fields = ('pet_name', 'pet_gender')


@admin.register(Contact)
class AdminPets(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_phone', 'contact_email')


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
    exclude = ('user_id',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user_id = request.user
        super().save_model(request, obj, form, change)


@admin.register(LostPets)
class AdminPets(admin.ModelAdmin):
    list_display = (
        'lost_pet_name', 'lost_pet_status', 'lost_pet_gender', 'lost_pet_age', 'lost_pet_lost_datetime')
    list_editable = ('lost_pet_status', 'lost_pet_age')
    list_filter = ('lost_pet_status', 'lost_pet_gender', 'lost_pet_lost_datetime')
    search_fields = ('lost_pet_name', 'lost_pet_gender')
    exclude = ('user_id',)


admin.site.register(Events)
