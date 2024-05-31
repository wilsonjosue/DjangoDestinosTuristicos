# gestion/forms.py
from django import forms
from .models import DestinosTuristicos

class DestinosTuristicosForm(forms.ModelForm):
    class Meta:
        model = DestinosTuristicos
        fields = ['nombreCiudad', 'descripcionCiudad', 'imagenCiudad', 'precioTour', 'ofertaTour']
