from django.db import models
# Create your models here.

class DestinosTuristicos(models.Model):
    nombreCiudad = models.CharField(max_length=100) #campo de texto corto
    descripcionCiudad = models.TextField()# Campo de texto largo
    imagenCiudad = models.ImageField(upload_to='images/')
    precioTour = models.DecimalField(max_digits=10, decimal_places=2)  # Corregido a decimal_places
    ofertaTour = models.BooleanField(default=False)

    def __str__(self):
        return self.nombreCiudad