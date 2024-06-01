# gestion/forms.py
from django import forms #Importa el módulo de formularios de Django.
from .models import DestinosTuristicos # Importa el modelo DestinosTuristicos desde el archivo models.py en la misma aplicación.

class DestinosTuristicosForm(forms.ModelForm):#Define una clase de formulario basada en un modelo de Django
    class Meta:
        model = DestinosTuristicos #Indica que este formulario se basa en el modelo DestinosTuristicos
        """Especifica una lista de campos del modelo que se deben incluir en el formulario. """
        fields = ['nombreCiudad', 'descripcionCiudad', 'imagenCiudad', 'precioTour', 'ofertaTour']    