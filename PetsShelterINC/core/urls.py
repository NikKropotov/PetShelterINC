from django.conf.urls import url

from . import views
from django.urls import path, include

from .views import MyRegisterFormView, logout_view

urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/register/', MyRegisterFormView.as_view(), name="signup_url"),
    path('accounts/logout/', logout_view, name="logout_url"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('pets', views.PetsListView.as_view(), name='pets_list'),
    path('found_pets', views.FoundPetsListView.as_view(), name='found_pets_list'),
    path('found_pets/add', views.add_found_pet, name='add_found_pets'),
    path('map', views.map),
    path('filter/', views.FilterPetsView.as_view(), name='filter'),
    path('json_filter/', views.JsonFilterPetsView.as_view(), name='json_filter'),
    path('pets/<int:idpet>/', views.pets_detail, name='pets_detail'),
    path('found_pets/<int:idfound_pet>/', views.found_pets_detail, name='found_pets_detail'),
]
