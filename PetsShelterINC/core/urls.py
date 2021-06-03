from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views
from .views import MyRegisterFormView, logout_view

urlpatterns = [
    path('', views.index, name="index"),
    path('help_page', views.help_page, name="help_page"),
    path('account', views.account, name="account"),
    path('edit/<int:idfound_pet>', views.update_f, name="edit_found_pets"),
    path('account/delete/found_pets/<int:idfound_pet>', views.destroy_f, name="destroy_found_pets"),
    path('edit/<int:idlost_pet>/', views.update_l, name="edit_lost_pets"),
    path('account/delete/lost_pets/<int:idlost_pet>', views.destroy_l, name="destroy_lost_pets"),
    path('accounts/register/', MyRegisterFormView.as_view(), name="signup_url"),
    path('accounts/logout/', logout_view, name="logout_url"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('pets', views.PetsListView.as_view(), name='pets_list'),
    path('found_pets', views.FoundPetsListView.as_view(), name='found_pets_list'),
    path('found_pets/add', views.add_found_pet, name='add_found_pets'),
    path('lost_pets', views.LostPetsListView.as_view(), name='lost_pets_list'),
    path('lost_pets/add', views.add_lost_pet, name='add_lost_pets'),
    path('map', views.map),
    path('filter/', views.FilterPetsView.as_view(), name='filter'),
    path('filter_f/', views.FoundFilterPetsView.as_view(), name='filter_f'),
    path('filter_l/', views.LostFilterPetsView.as_view(), name='filter_l'),
    path('json_filter/', views.JsonFilterPetsView.as_view(), name='json_filter'),
    path('pets/<int:idpet>/', views.pets_detail, name='pets_detail'),
    path('found_pets/<int:idfound_pet>/', views.found_pets_detail, name='found_pets_detail'),
    path('lost_pets/<int:idlost_pet>/', views.lost_pets_detail, name='lost_pets_detail'),
]
