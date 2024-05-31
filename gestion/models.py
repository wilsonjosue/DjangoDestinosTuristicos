from django.db import models
# Create your models here.

class DistinosTuristicos(models.Model):
    nombreCiudad = models.CharField(max_lenght=100) #campo de texto corto
    descripcionCiudad = models.TextField()# Campo de texto largo
    imagenCiudad = models.ImageField(upload_to='images/')
    precioTour = models.DecimalField(max_digits=10, dicimal_place=2)
    ofertaTour = models.BooleanField(default=False)

    def __str__(self):
        return self.nombreCiudad