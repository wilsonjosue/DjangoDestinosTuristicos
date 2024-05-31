# gestion/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarDestinos, name='listarDestinos'),
    path('añadir/', views.añadirDestino, name='añadirDestino'),
    path('modificar/<int:id>/', views.modificarDestino, name='modificarDestino'),
    path('eliminar/<int:id>/', views.eliminarDestino, name='eliminarDestino'),
]