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
    path('map', views.map),
    path('filter/', views.FilterPetsView.as_view(), name='filter_breed'),
    path('pets/<int:idpet>/', views.pets_detail, name='pets_detail'),

]
