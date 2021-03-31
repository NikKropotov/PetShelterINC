from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('pets', views.pets),
    path('map', views.map),
]
