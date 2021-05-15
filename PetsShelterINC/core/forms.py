from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class AddFoundPetForm(forms.ModelForm):
    class Meta:
        model = FoundPets
        exclude = ["found_pet_found_datetime", "user_id"]
        fields = (
            'found_pet_name', 'found_pet_breed', 'found_pet_color', 'found_pet_gender', 'found_pet_size',
            'found_pet_age', 'found_pet_health', 'found_pet_description', 'found_pet_found_location',
            'found_contact_name', 'found_contact_phone', 'found_contact_email', 'found_petImagePath'
        )


class EditFoundPetForm(forms.ModelForm):
    class Meta:
        model = FoundPets
        fields = '__all__'
        exclude = ["found_pet_found_datetime", "user_id"]
        widgets = {
            'found_pet_name': forms.TextInput(attrs={'class': 'form-control'}),
            'found_pet_status': forms.Select(attrs={'class': 'form-control'}),
            'found_pet_breed': forms.TextInput(attrs={'class': 'form-control'}),
            'found_pet_color': forms.TextInput(attrs={'class': 'form-control'}),
            'found_pet_gender': forms.Select(attrs={'class': 'form-control'}),
            'found_pet_size': forms.Select(attrs={'class': 'form-control'}),
            'found_pet_age': forms.TextInput(attrs={'class': 'form-control'}),
            'found_pet_health': forms.TextInput(attrs={'class': 'form-control'}),
            'found_pet_description': forms.Textarea(attrs={'class': 'form-control'}),
            'found_pet_found_location': forms.TextInput(attrs={'class': 'form-control'}),
            'found_contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'found_contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'found_contact_email': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        found_pets = self.instance
        found_pets.found_pet_name = self.cleaned_data["found_pet_name"]
        found_pets.found_pet_status = self.cleaned_data["found_pet_status"]
        found_pets.found_pet_breed = self.cleaned_data['found_pet_breed']
        found_pets.found_pet_color = self.cleaned_data['found_pet_color']
        found_pets.found_pet_gender = self.cleaned_data["found_pet_gender"]
        found_pets.found_pet_size = self.cleaned_data["found_pet_size"]
        found_pets.found_pet_age = self.cleaned_data["found_pet_age"]
        found_pets.found_pet_health = self.cleaned_data["found_pet_health"]
        found_pets.found_pet_description = self.cleaned_data["found_pet_description"]
        found_pets.found_pet_found_location = self.cleaned_data["found_pet_found_location"]
        found_pets.found_contact_name = self.cleaned_data["found_contact_name"]
        found_pets.found_contact_phone = self.cleaned_data["found_contact_phone"]
        found_pets.found_contact_email = self.cleaned_data["found_contact_email"]
        if self.cleaned_data["found_petImagePath"]:
            found_pets.found_petImagePath = self.cleaned_data["found_petImagePath"]
        if commit:
            found_pets.save()
        return found_pets


class AddLostPetForm(forms.ModelForm):
    class Meta:
        lost_petImagePath = forms.TextInput(
            attrs={'type': 'file', 'accept': 'image/*', 'id': 'id_lost_petImagePath'})
        model = LostPets
        exclude = ["lost_pet_lost_datetime", "user_id"]
        fields = (
            'lost_pet_name', 'lost_pet_breed', 'lost_pet_size', 'lost_pet_gender', 'lost_pet_age', 'lost_pet_color',
            'lost_pet_description', 'lost_pet_lost_location', 'lost_contact_name',
            'lost_contact_phone', 'lost_contact_email', 'lost_petImagePath')


class EditLostPetForm(forms.ModelForm):
    class Meta:
        model = LostPets
        fields = '__all__'
        exclude = ["lost_pet_lost_datetime", "user_id"]
        widgets = {
            'lost_pet_name': forms.TextInput(attrs={'class': 'form-control'}),
            'lost_pet_status': forms.Select(attrs={'class': 'form-control'}),
            'lost_pet_breed': forms.TextInput(attrs={'class': 'form-control'}),
            'lost_pet_color': forms.TextInput(attrs={'class': 'form-control'}),
            'lost_pet_gender': forms.Select(attrs={'class': 'form-control'}),
            'lost_pet_size': forms.Select(attrs={'class': 'form-control'}),
            'lost_pet_age': forms.TextInput(attrs={'class': 'form-control'}),
            'lost_pet_description': forms.Textarea(attrs={'class': 'form-control'}),
            'lost_pet_lost_location': forms.TextInput(attrs={'class': 'form-control'}),
            'lost_contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'lost_contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'lost_contact_email': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        lost_pets = self.instance
        lost_pets.lost_pet_name = self.cleaned_data["lost_pet_name"]
        lost_pets.lost_pet_status = self.cleaned_data["lost_pet_status"]
        lost_pets.lost_pet_breed = self.cleaned_data['lost_pet_breed']
        lost_pets.lost_pet_color = self.cleaned_data['lost_pet_color']
        lost_pets.lost_pet_gender = self.cleaned_data["lost_pet_gender"]
        lost_pets.lost_pet_size = self.cleaned_data["lost_pet_size"]
        lost_pets.lost_pet_age = self.cleaned_data["lost_pet_age"]
        lost_pets.lost_pet_description = self.cleaned_data["lost_pet_description"]
        lost_pets.lost_pet_lost_location = self.cleaned_data["lost_pet_lost_location"]
        lost_pets.lost_contact_name = self.cleaned_data["lost_contact_name"]
        lost_pets.lost_contact_phone = self.cleaned_data["lost_contact_phone"]
        lost_pets.lost_contact_email = self.cleaned_data["lost_contact_email"]
        if self.cleaned_data["lost_petImagePath"]:
            lost_pets.lost_petImagePath = self.cleaned_data["lost_petImagePath"]
        if commit:
            lost_pets.save()
        return lost_pets
