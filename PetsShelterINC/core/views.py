from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView
from django.contrib.auth import logout
from django.views.generic import ListView

from core.models import *


# Главная страница.
def index(request):
    return render(request, 'core/index.html')


# Вывод пород
class PetsBreedView:
    def get_pets_breeds(self):
        return Pets.objects.values('pet_breed').distinct()


# Вывод анкет животных
class PetsListView(PetsBreedView, ListView):
    queryset = Pets.objects.all()
    context_object_name = 'pets'
    paginate_by = 3
    template_name = 'core/pets.html'


# Детали анкеты
def pets_detail(request, idpet):
    pet_detail = get_object_or_404(Pets,
                                   idpet=idpet)
    return render(request, 'core/pet_detail.html', {'pet_detail': pet_detail})


# Карта
def map(request):
    return render(request, 'core/map.html')


# Авторизация и регистраци
class MyRegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/accounts/login/"
    template_name = "registration.html"

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
class FilterPetsView(PetsBreedView, ListView):
    def get_queryset(self):
        queryset = Pets.objects.filter(pet_breed__in=self.request.GET.getlist("pet_breed"))
        return queryset
