from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import DestinosTuristicos# Importa el modelo DestinosTuristicos desde el archivo models.py en la misma aplicación.
from .forms import DestinosTuristicosForm# Importa el modelo DestinosTuristicosForm desde el archivo forms.py 
# Create your views here.
"""index"""
def index(request):
    return render(request,"index.html",{'dests':dests})

"""Esta vista lista todos los destinos turísticos."""
def listarDestinos(request):
    destinos = DestinosTuristicos.objects.all()#para obtener todos los registros del modelo DestinosTuristicos.
    return render(request,'destinations.html',{'destinos': destinos})

"""Permite añadir un nuevo destino turístico."""
def añadirDestino(request):
    if request.method == 'POST':
        #Intenta crear un formulario con los datos proporcionados.
        form = DestinosTuristicosForm(request.POST, request.FILES)
        if form.is_valid():#Si es valido el form
            form.save() #Guarda el nuevo destino  
            return redirect('listarDestinos')#Redirige a la vista listarDestinos.
    else:
        form = DestinosTuristicosForm()#muestra un formulario vacío.
    return render(request, 'añadirDestino.html', {'form': form}) 

"""Permite modificar un destino turístico existente."""
def modificarDestino(request, id):
    #Obtiene el destino correspondiente al id proporcionado, o muestra un error 404 si no existe.
    destino = get_object_or_404(DestinosTuristicos, id=id)
    #Si el método de la solicitud es POST, intenta actualizar el destino con los datos proporcionados.
    if request.method == 'POST':
        form = DestinosTuristicosForm(request.POST, request.FILES, instance=destino)
        if form.is_valid():#Si es valido el form.
            form.save() #Guarda los cambio.
            return redirect('listarDestinos')#Redirige a la vista listarDestinos.
    else:
        #Muestra un formulario con los datos existentes del destino.
        form = DestinosTuristicosForm(instance=destino)#Renderiza el template añadirDestino.html
    return render(request, 'añadirDestino.html', {'form': form})

"""Permite eliminar un destino turístico."""
def eliminarDestino(request, id):
    #Obtiene el destino correspondiente al id proporcionado, o muestra un error 404 si no existe.
    destino = get_object_or_404(DestinosTuristicos, id=id)
    if request.method == 'POST':
        destino.delete()#Elimina el destino 
        return redirect('listarDestinos')#Redirige a la vista listarDestinos.
    return render(request, 'eliminarDestino.html', {'destino': destino})
