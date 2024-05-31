from django.db import models
# Create your models here.

class DistinosTuristicos(models.Model):

    nombreCiudad = models.CharField(max_lenght = 100) #campo de texto corto
    descripcionCiudad = models.TextField()# Campo de texto largo
    imagenCiudad = models.ImageField(upload_to = 'images/')
    precioTour =
    ofertaTour =





