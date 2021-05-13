from PIL.Image import new
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.contrib.auth import logout
from django.views.generic import ListView
from bootstrap_modal_forms.generic import BSModalCreateView

from core.forms import AddFoundPetForm
from core.models import *


# Главная страница.
def index(request):
    return render(request, 'core/index.html')


# Вывод данных
class PetsGetDataFilterView:
    template_name = 'core/pets_list.html'

    def get_pets_breeds(self):
        return PetsBreed.objects.all()

    def get_pets_genders(self):
        return Pets.objects.all().distinct().values("pet_gender")

    def get_pets_size(self):
        return Pets.objects.all().distinct().values("pet_size")

    def get_pets_type(self):
        return Pets.objects.all().distinct().values("pet_type")

    def get_pets_temp(self):
        return Pets.objects.all().distinct().values("pet_temperament")

    def get_pets_wool_length(self):
        return Pets.objects.all().distinct().values("pet_wool_length")

    def get_pet_wool_color(self):
        return Pets.objects.all().distinct().values("pet_wool_color")

    def get_pet_wool_color_extra(self):
        return Pets.objects.all().distinct().values("pet_wool_color_extra")

    def get_pet_health(self):
        return Pets.objects.all().distinct().values("pet_health")

    def get_pet_vaccination(self):
        return Pets.objects.all().distinct().values("pet_vaccination")

    def get_pet_sterilization(self):
        return Pets.objects.all().distinct().values("pet_sterilization")

    def get_pet_attitude_children(self):
        return Pets.objects.all().distinct().values("pet_attitude_children")

    def get_pet_attitude_cat(self):
        return Pets.objects.all().distinct().values("pet_attitude_cat")

    def get_attitude_other_pets(self):
        return Pets.objects.all().distinct().values("attitude_other_pets")


# Вывод анкет животных
class PetsListView(PetsGetDataFilterView, ListView):
    queryset = Pets.objects.all()
    context_object_name = 'pets'
    paginate_by = 3
    template_name = 'core/pets_list.html'


# Вывод анкет животных
class FoundPetsListView(ListView):
    queryset = FoundPets.objects.all()
    context_object_name = 'found_pets'
    paginate_by = 3
    template_name = 'core/found_pets_list.html'


# Детали анкеты
def pets_detail(request, idpet):
    pets_d = Pets.objects.all().select_related('contact_idcontact')
    pet_detail = get_object_or_404(pets_d,
                                   idpet=idpet)
    return render(request, 'core/pets_detail.html', {'pet_detail': pet_detail})


# Детали анкеты
def found_pets_detail(request, idfound_pet):
    pets_f = FoundPets.objects.all()
    found_pet_detail = get_object_or_404(pets_f,
                                         idfound_pet=idfound_pet)
    return render(request, 'core/found_pets_detail.html', {'found_pet_detail': found_pet_detail})


# Карта
def map(request):
    return render(request, 'core/map.html')


# Авторизация и регистраци
class MyRegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/accounts/login/"
    template_name = "registration/registration.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


def logout_view(request):
    logout(request)
    return redirect('index')


def regist(request):
    return render(request, 'registration/../templates/registration.html')


# Фильтры
class FilterPetsView(PetsListView, ListView):
    model = Pets
    paginate_by = 3

    def get_queryset(self):
        queryset = Pets.objects.all()
        if "breeds" in self.request.GET:
            queryset = queryset.filter(pet_breed_idpet_breed__in=self.request.GET.getlist("breeds"))
        if "genders" in self.request.GET:
            queryset = queryset.filter(pet_gender__in=self.request.GET.getlist("genders"))
        if "sizes" in self.request.GET:
            queryset = queryset.filter(pet_size__in=self.request.GET.getlist("sizes"))
        if "types" in self.request.GET:
            queryset = queryset.filter(pet_type__in=self.request.GET.getlist("types"))
        if "temps" in self.request.GET:
            queryset = queryset.filter(pet_temperament__in=self.request.GET.getlist("temps"))
        if "wool_lengths" in self.request.GET:
            queryset = queryset.filter(pet_wool_length__in=self.request.GET.getlist("wool_lengths"))
        if "wool_colors" in self.request.GET:
            queryset = queryset.filter(pet_wool_color__in=self.request.GET.getlist("wool_colors"))
        if "wool_colors_extras" in self.request.GET:
            queryset = queryset.filter(pet_wool_color_extra__in=self.request.GET.getlist("wool_colors_extras"))
        if "healths" in self.request.GET:
            queryset = queryset.filter(pet_health__in=self.request.GET.getlist("healths"))
        if "sters" in self.request.GET:
            queryset = queryset.filter(pet_sterilization__in=self.request.GET.getlist("sters"))
        if "vaccs" in self.request.GET:
            queryset = queryset.filter(pet_vaccination__in=self.request.GET.getlist("vaccs"))
        if "ch_atts" in self.request.GET:
            queryset = queryset.filter(pet_attitude_children__in=self.request.GET.getlist("ch_atts"))
        if "cat_atts" in self.request.GET:
            queryset = queryset.filter(pet_attitude_cat__in=self.request.GET.getlist("cat_atts"))
        if "other_atts" in self.request.GET:
            queryset = queryset.filter(pet_attitude_other_pets__in=self.request.GET.getlist("other_atts"))
        return queryset
        # queryset = Pets.objects.filter(
        #     Q(pet_breed_idpet_breed__in=self.request.GET.getlist("breeds")) |
        #     Q(pet_gender__in=self.request.GET.getlist("genders")) |
        #     Q(pet_size__in=self.request.GET.getlist("sizes")) |
        #     Q(pet_type__in=self.request.GET.getlist("types")) |
        #     Q(pet_temperament__in=self.request.GET.getlist("temps")) |
        #     Q(pet_wool_length__in=self.request.GET.getlist("wool_lengths")) |
        #     Q(pet_wool_color__in=self.request.GET.getlist("wool_colors")) |
        #     Q(pet_wool_color_extra__in=self.request.GET.getlist("wool_colors_extras"))
        # ).distinct()
        # return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["breeds"] = ''.join(f"breeds={x}&" for x in self.request.GET.getlist("breeds"))
        context["genders"] = ''.join(f"genders={x}&" for x in self.request.GET.getlist("genders"))
        context["sizes"] = ''.join(f"sizes={x}&" for x in self.request.GET.getlist("sizes"))
        context["types"] = ''.join(f"types={x}&" for x in self.request.GET.getlist("types"))
        context["temps"] = ''.join(f"temps={x}&" for x in self.request.GET.getlist("temps"))
        context["wool_lengths"] = ''.join(f"wool_lengths={x}&" for x in self.request.GET.getlist("wool_lengths"))
        context["wool_colors"] = ''.join(f"wool_colors={x}&" for x in self.request.GET.getlist("wool_colors"))
        context["wool_colors_extras"] = ''.join(
            f"wool_colors_extras={x}&" for x in self.request.GET.getlist("wool_colors_extras"))
        context["healths"] = ''.join(f"healths={x}&" for x in self.request.GET.getlist("healths"))
        context["sters"] = ''.join(f"sters={x}&" for x in self.request.GET.getlist("sters"))
        context["vaccs"] = ''.join(f"vaccs={x}&" for x in self.request.GET.getlist("vaccs"))
        context["ch_atts"] = ''.join(f"ch_atts={x}&" for x in self.request.GET.getlist("ch_atts"))
        context["cat_atts"] = ''.join(f"cat_atts={x}&" for x in self.request.GET.getlist("cat_atts"))
        context["other_atts"] = ''.join(f"other_atts={x}&" for x in self.request.GET.getlist("other_atts"))
        return context


class JsonFilterPetsView(PetsGetDataFilterView, ListView):
    model = Pets
    template_name = 'core/pets_list.html'

    def get_queryset(self):
        queryset = Pets.objects.filter(
            Q(pet_breed_idpet_breed__in=self.request.GET.getlist("breeds"))
        ).distinct().values("pet_status", "petImagePath", "pet_name", "idpet")
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"pets": queryset}, safe=False)


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def add_found_pet(request):
    if request.method == "POST":
        form = AddFoundPetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('found_pets_list')
    else:
        form = AddFoundPetForm()
    return render(request, 'core/add_found_form.html', {'form': form})

# def add_found_pets(request):
#     form = AddFoundPetForm(request.POST or None)
#     if form.is_valid():
#         response = JsonResponse({"message": 'success'})
#         response.status_code = 201
#         return render(request, 'core/found_pets_list.html', {'form': form})
#     else:
#         response = JsonResponse({"errors": form.errors.as_json()})
#         response.status_code = 403
#         return response

# if request.method == 'POST':
#     form = AddFoundPetForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect('core/found_pets_detail.html')
# else:
#     form = AddFoundPetForm()
#
# context = {'form': form}
# return render(request, 'core/found_pets_list.html', context)


# def add_found_pet(request):
#     context = {"data_f": FoundPets.objects.all()}
#     found_pets = FoundPets()
#     form = AddFoundPetForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             found_pets.found_pet_name = form.cleaned_data.get("found_pet_name")
#             found_pets.found_pet_breed = form.cleaned_data.get("found_pet_breed")
#             found_pets.found_pet_color = form.cleaned_data.get("found_pet_color")
#             found_pets.found_pet_gender = form.cleaned_data.get("found_pet_gender")
#             found_pets.found_pet_size = form.cleaned_data.get("found_pet_size")
#             found_pets.found_pet_age = form.cleaned_data.get("found_pet_age")
#             found_pets.found_pet_found_datetime = form.cleaned_data.get("found_pet_found_datetime")
#             found_pets.found_pet_health = form.cleaned_data.get("found_pet_health")
#             found_pets.found_pet_description = form.cleaned_data.get("found_pet_description")
#             found_pets.found_pet_found_location = form.cleaned_data.get("found_pet_found_location")
#             found_pets.found_contact_name = form.cleaned_data.get("found_contact_name")
#             found_pets.found_contact_phone = form.cleaned_data.get("found_contact_phone")
#             found_pets.found_contact_email = form.cleaned_data.get("found_contact_email")
#             found_pets.found_petImagePath = form.cleaned_data.get("found_petImagePath")
#             found_pets.save()
#             messages.add_message(request, messages.INFO, "Анкета добавлена")
#             return redirect('core/found_pets_detail.html')
#         else:
#             form = AddFoundPetForm()
#     context['form'] = form
#     # context['form'] = new_found_pet
#     return render(request, 'core/add_found_form.html', context)


# def add_found_pets(self, request, *args, **kwargs):
#     found_pet = FoundPets.objects.all()
#     if request.method == 'POST':
#         form = AddFoundPetForm(request.POST or None)
#         if form.is_valid():
#             new_found_pet = form.save(commit=False)
#             new_found_pet.found_pet_name = form.cleaned_data['found_pet_name']
#             new_found_pet.found_pet_breed = form.cleaned_data['found_pet_breed']
#             new_found_pet.found_pet_color = form.cleaned_data['found_pet_color']
#             new_found_pet.found_pet_gender = form.cleaned_data['found_pet_gender']
#             new_found_pet.found_pet_size = form.cleaned_data['found_pet_size']
#             new_found_pet.found_pet_age = form.cleaned_data['found_pet_age']
#             new_found_pet.found_pet_found_datetime = form.cleaned_data['found_pet_found_datetime']
#             new_found_pet.found_pet_health = form.cleaned_data['found_pet_health']
#             new_found_pet.found_pet_description = form.cleaned_data['found_pet_description']
#             new_found_pet.found_pet_found_location = form.cleaned_data['found_pet_found_location']
#             new_found_pet.found_contact_name = form.cleaned_data['found_contact_name']
#             new_found_pet.found_contact_phone = form.cleaned_data['found_contact_phone']
#             new_found_pet.found_contact_email = form.cleaned_data['found_contact_email']
#             new_found_pet.found_petImagePath = form.cleaned_data['found_petImagePath']
#             new_found_pet.save()
#             found_pet.add(new_found_pet)
#             messages.add_message(request, messages.INFO, "Анкета добавлена")
#             return HttpResponseRedirect('core/found_pets_list.html')
#         return HttpResponseRedirect('core/found_pets_list.html')

# return redirect('core/found_pets_detail.html')
# else:
#     form = AddFoundPetForm()
#
# context = {'form': form}
# return render(request, 'core/found_pets_list.html', context)
