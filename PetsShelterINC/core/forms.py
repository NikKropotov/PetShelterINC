from django import forms
from django.forms import ModelForm

from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from bootstrap_modal_forms.forms import BSModalModelForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class AddFoundPetForm(forms.ModelForm):
    class Meta:
        found_petImagePath = forms.TextInput(attrs={'type': 'file', 'accept': 'image/*', 'id': 'id_found_petImagePath'})
        model = FoundPets
        fields = (
            'found_pet_name', 'found_pet_breed', 'found_pet_color', 'found_pet_gender', 'found_pet_size',
            'found_pet_age',
            'found_pet_found_datetime', 'found_pet_health', 'found_pet_description', 'found_pet_found_location',
            'found_contact_name', 'found_contact_phone', 'found_contact_email', 'found_petImagePath'
        )
        # widgets = {
        #     'found_pet_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'found_pet_breed': forms.TextInput(attrs={'class': 'form-control'}),
        #     'found_pet_color': forms.TextInput(attrs={'class': 'form-control'}),
        #     'found_pet_gender': forms.Select(attrs={'class': 'form-control'}),
        #     'found_pet_size': forms.Select(attrs={'class': 'form-control'}),
        #     'found_pet_age': forms.TextInput(attrs={'class': 'form-control'}),
        #     'found_pet_found_datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime'}),
        #     'found_pet_health': forms.TextInput(attrs={'class': 'form-control'}),
        #     'found_pet_description': forms.TextInput(attrs={'class': 'form-control'}),
        #     'found_pet_found_location': forms.TextInput(attrs={'class': 'form-control'}),
        #     'found_contact_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'found_contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
        #     'found_contact_email': forms.TextInput(attrs={'class': 'form-control'}),
        #     'found_petImagePath': forms.TextInput(attrs={'type': 'file'}),
        # }
