from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView
from django.views.generic import ListView

from core.forms import AddFoundPetForm, AddLostPetForm, EditFoundPetForm, EditLostPetForm
from core.models import *


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
    return render(request, 'registration/registration.html')


# Главная страница.
def index(request):
    return render(request, 'core/index.html')


# Главная страница.
def help_page(request):
    return render(request, 'core/help.html')


# Страница аккаунта.
def account(request):
    context = {
        'found_pets': FoundPets.objects.all().order_by('-found_pet_found_datetime').filter(user_id=request.user),
        'lost_pets': LostPets.objects.all().order_by('-lost_pet_lost_datetime').filter(user_id=request.user)
    }
    return render(request, 'core/account.html', context)


# Функция изменения анкет пропавших животных.
def update_f(request, idfound_pet):
    contex = {}
    found_pets = get_object_or_404(FoundPets,
                                   idfound_pet=idfound_pet)
    if request.POST:
        form = EditFoundPetForm(request.POST or None, request.FILES or None, instance=found_pets)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            contex['success_message'] = "Данные обновлены"
            found_pets = obj
    form = EditFoundPetForm(
        initial={
            "found_pet_name": found_pets.found_pet_name,
            "found_pet_status": found_pets.found_pet_status,
            "found_pet_breed": found_pets.found_pet_breed,
            "found_pet_color": found_pets.found_pet_color,
            "found_pet_gender": found_pets.found_pet_gender,
            "found_pet_size": found_pets.found_pet_size,
            "found_pet_age": found_pets.found_pet_age,
            "found_pet_health": found_pets.found_pet_health,
            "found_pet_description": found_pets.found_pet_description,
            "found_pet_found_location": found_pets.found_pet_found_location,
            "found_contact_name": found_pets.found_contact_name,
            "found_contact_phone": found_pets.found_contact_phone,
            "found_contact_email": found_pets.found_contact_email,
            "found_petImagePath": found_pets.found_petImagePath,
        }
    )
    contex['form'] = form
    return render(request, "core/edit_found_form.html", contex)


# Функция удаления анкет пропавших животных.
def destroy_f(request, idfound_pet):
    found_pets = FoundPets.objects.get(idfound_pet=idfound_pet)
    found_pets.delete()
    return redirect("/account")


# Функция изменения анкет пропавших животных.
def update_l(request, idlost_pet):
    contex = {}
    lost_pets = get_object_or_404(LostPets,
                                  idlost_pet=idlost_pet)
    if request.POST:
        form = EditLostPetForm(request.POST or None, request.FILES or None, instance=lost_pets)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            contex['success_message'] = "Данные обновлены"
            lost_pets = obj
    form = EditLostPetForm(
        initial={
            "lost_pet_name": lost_pets.lost_pet_name,
            "lost_pet_status": lost_pets.lost_pet_status,
            "lost_pet_breed": lost_pets.lost_pet_breed,
            "lost_pet_color": lost_pets.lost_pet_color,
            "lost_pet_gender": lost_pets.lost_pet_gender,
            "lost_pet_size": lost_pets.lost_pet_size,
            "lost_pet_age": lost_pets.lost_pet_age,
            "lost_pet_description": lost_pets.lost_pet_description,
            "lost_pet_lost_location": lost_pets.lost_pet_lost_location,
            "lost_contact_name": lost_pets.lost_contact_name,
            "lost_contact_phone": lost_pets.lost_contact_phone,
            "lost_contact_email": lost_pets.lost_contact_email,
            "lost_petImagePath": lost_pets.lost_petImagePath,
        }
    )
    contex['form'] = form
    return render(request, "core/edit_lost_form.html", contex)


# Функция удаления анкет пропавших животных.
def destroy_l(request, idlost_pet):
    lost_pets = LostPets.objects.get(idlost_pet=idlost_pet)
    lost_pets.delete()
    return redirect("/account")


# Фильтры
class PetsGetDataFilterView:
    template_name = 'core/pets_list.html'

    def get_pets_breeds(self):
        return Pets.objects.all().distinct().values("pet_breed")

    def get_pets_ages(self):
        return Pets.objects.all().distinct().values("pet_age").order_by("pet_age")

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
    paginate_by = 6
    template_name = 'core/pets_list.html'


# Детали анкеты
def pets_detail(request, idpet):
    pets_d = Pets.objects.all().select_related('contact_idcontact')
    pet_detail = get_object_or_404(pets_d,
                                   idpet=idpet)
    return render(request, 'core/pets_detail.html', {'pet_detail': pet_detail})


# Карта
def map(request):
    return render(request, 'core/map.html')


# Фильтры
class FoundPetsGetDataFilterView:
    template_name = 'core/found_pets_list.html'

    def get_found_pets_breeds(self):
        return FoundPets.objects.all().distinct().values("found_pet_breed")

    def get_found_pets_ages(self):
        return FoundPets.objects.all().distinct().values("found_pet_age").order_by("found_pet_age")

    def get_found_pets_genders(self):
        return FoundPets.objects.all().distinct().values("found_pet_gender")

    def get_found_pets_size(self):
        return FoundPets.objects.all().distinct().values("found_pet_size")

    def get_found_pets_color(self):
        return FoundPets.objects.all().distinct().values("found_pet_color")

    def get_found_pets_date(self):
        return FoundPets.objects.all().distinct().values("found_pet_found_datetime")


# Вывод анкет найденных животных
class FoundPetsListView(FoundPetsGetDataFilterView, ListView):
    queryset = FoundPets.objects.all().order_by('-found_pet_found_datetime')
    context_object_name = 'found_pets'
    paginate_by = 6
    template_name = 'core/found_pets_list.html'


# Детали анкеты найденных животных
def found_pets_detail(request, idfound_pet):
    pets_f = FoundPets.objects.all()
    found_pet_detail = get_object_or_404(pets_f,
                                         idfound_pet=idfound_pet)
    return render(request, 'core/found_pets_detail.html', {'found_pet_detail': found_pet_detail})


# Добавление анкеты найденных животных
@login_required
def add_found_pet(request):
    if request.method == "POST":
        form = AddFoundPetForm(request.POST, request.FILES)
        if form.is_valid():
            new_f = form.save(commit=False)
            new_f.user_id = request.user
            new_f.save()
            return redirect('found_pets_list')
    else:
        form = AddFoundPetForm()
    return render(request, 'core/add_found_form.html', {'form': form})


# Фильтры
class LostPetsGetDataFilterView:
    template_name = 'core/lost_pets_list.html'

    def get_found_pets_breeds(self):
        return LostPets.objects.all().distinct().values("lost_pet_breed")

    def get_found_pets_ages(self):
        return LostPets.objects.all().distinct().values("lost_pet_age").order_by("lost_pet_age")

    def get_found_pets_genders(self):
        return LostPets.objects.all().distinct().values("lost_pet_gender")

    def get_found_pets_size(self):
        return LostPets.objects.all().distinct().values("lost_pet_size")

    def get_found_pets_color(self):
        return LostPets.objects.all().distinct().values("lost_pet_color")

    def get_found_pets_date(self):
        return LostPets.objects.all().distinct().values("lost_pet_lost_datetime")


# Вывод анкет найденных животных
class LostPetsListView(LostPetsGetDataFilterView, ListView):
    queryset = LostPets.objects.all()
    context_object_name = 'lost_pets'
    paginate_by = 6
    template_name = 'core/lost_pets_list.html'


# Детали анкеты найденных животных
def lost_pets_detail(request, idlost_pet):
    pets_l = LostPets.objects.all()
    lost_pet_detail = get_object_or_404(pets_l,
                                        idlost_pet=idlost_pet)
    return render(request, 'core/lost_pets_detail.html', {'lost_pet_detail': lost_pet_detail})


# Добавление анкеты найденных животных
@login_required
def add_lost_pet(request):
    if request.method == "POST":
        form = AddLostPetForm(request.POST, request.FILES)
        if form.is_valid():
            new_f = form.save(commit=False)
            new_f.user_id = request.user
            new_f.save()
            return redirect('lost_pets_list')
    else:
        form = AddLostPetForm()
    return render(request, 'core/add_lost_form.html', {'form': form})


# Фильтры анкет животных
class FilterPetsView(PetsListView, ListView):
    model = Pets
    paginate_by = 6

    def get_queryset(self):
        queryset = Pets.objects.all()
        if "breeds" in self.request.GET:
            queryset = queryset.filter(pet_breed__in=self.request.GET.getlist("breeds"))
        if "ages" in self.request.GET:
            queryset = queryset.filter(pet_age__in=self.request.GET.getlist("ages"))
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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["breeds"] = ''.join(f"breeds={x}&" for x in self.request.GET.getlist("breeds"))
        context["ages"] = ''.join(f"ages={x}&" for x in self.request.GET.getlist("ages"))
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


class FoundFilterPetsView(FoundPetsListView, ListView):
    model = FoundPets
    paginate_by = 6

    def get_queryset(self):
        queryset = FoundPets.objects.all()
        if "breeds" in self.request.GET:
            queryset = queryset.filter(found_pet_breed__in=self.request.GET.getlist("breeds"))
        if "ages" in self.request.GET:
            queryset = queryset.filter(found_pet_age__in=self.request.GET.getlist("ages"))
        if "genders" in self.request.GET:
            queryset = queryset.filter(found_pet_gender__in=self.request.GET.getlist("genders"))
        if "sizes" in self.request.GET:
            queryset = queryset.filter(found_pet_size__in=self.request.GET.getlist("sizes"))
        if "colors" in self.request.GET:
            queryset = queryset.filter(found_pet_color__in=self.request.GET.getlist("colors"))
        if "dates" in self.request.GET:
            queryset = queryset.filter(found_pet_found_datetime__in=self.request.GET.getlist("dates"))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["breeds"] = ''.join(f"breeds={x}&" for x in self.request.GET.getlist("breeds"))
        context["ages"] = ''.join(f"ages={x}&" for x in self.request.GET.getlist("ages"))
        context["genders"] = ''.join(f"genders={x}&" for x in self.request.GET.getlist("genders"))
        context["sizes"] = ''.join(f"sizes={x}&" for x in self.request.GET.getlist("sizes"))
        context["colors"] = ''.join(f"colors={x}&" for x in self.request.GET.getlist("colors"))
        context["dates"] = ''.join(f"dates={x}&" for x in self.request.GET.getlist("dates"))
        return context


class LostFilterPetsView(LostPetsListView, ListView):
    model = LostPets
    paginate_by = 6

    def get_queryset(self):
        queryset = LostPets.objects.all()
        if "breeds" in self.request.GET:
            queryset = queryset.filter(lost_pet_breed__in=self.request.GET.getlist("breeds"))
        if "ages" in self.request.GET:
            queryset = queryset.filter(lost_pet_age__in=self.request.GET.getlist("ages"))
        if "genders" in self.request.GET:
            queryset = queryset.filter(lost_pet_gender__in=self.request.GET.getlist("genders"))
        if "sizes" in self.request.GET:
            queryset = queryset.filter(lost_pet_size__in=self.request.GET.getlist("sizes"))
        if "colors" in self.request.GET:
            queryset = queryset.filter(lost_pet_color__in=self.request.GET.getlist("colors"))
        if "dates" in self.request.GET:
            queryset = queryset.filter(lost_pet_lost_datetime__in=self.request.GET.getlist("dates"))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["breeds"] = ''.join(f"breeds={x}&" for x in self.request.GET.getlist("breeds"))
        context["ages"] = ''.join(f"ages={x}&" for x in self.request.GET.getlist("ages"))
        context["genders"] = ''.join(f"genders={x}&" for x in self.request.GET.getlist("genders"))
        context["sizes"] = ''.join(f"sizes={x}&" for x in self.request.GET.getlist("sizes"))
        context["colors"] = ''.join(f"colors={x}&" for x in self.request.GET.getlist("colors"))
        context["dates"] = ''.join(f"dates={x}&" for x in self.request.GET.getlist("dates"))
        return context
