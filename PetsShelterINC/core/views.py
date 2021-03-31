from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.views.generic import FormView
from django.contrib.auth import logout

from core.models import *


# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def pets(request):
    try:
        p = Pets.objects.all()
    except:
        raise Http404("Данные не загружены")
    return render(request, 'core/pets.html', {'pets': p})


def map(request):
    return render(request, 'core/map.html')


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
