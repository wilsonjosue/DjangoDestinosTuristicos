# gestion/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarDestinos, name='listarDestinos'),# Ruta, lista los destinos turísticos.
    path('añadir/', views.añadirDestino, name='añadirDestino'),#Ruta, añade un destino turístico.
    path('modificar/<int:id>/', views.modificarDestino, name='modificarDestino'),#Ruta, modifica un destino existente
    path('eliminar/<int:id>/', views.eliminarDestino, name='eliminarDestino'),#Ruta, elimina un destino existente
]