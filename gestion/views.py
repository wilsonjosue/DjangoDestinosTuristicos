from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import DestinosTuristicos# Importa el modelo DestinosTuristicos desde el archivo models.py en la misma aplicación.
from .forms import DestinosTuristicosForm# Importa el modelo DestinosTuristicosForm desde el archivo forms.py 
# Create your views here.
"""Esta vista lista todos los destinos turísticos."""
def listarDestinos(request):
    destinos = DestinosTuristicos.objects.all()#para obtener todos los registros del modelo DestinosTuristicos.
    return render(request,'destinations.html',{'destinos': destinos})

def añadirDestino(request):
    if request.method == 'POST':
        form = DestinosTuristicosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listarDestinos')
    else:
        form =  DestinosTuristicosForm()
    return render(request, 'añadirDestino.html', {'form': form}) 

def modificarDestino(request, id):
    destino = get_object_or_404(DestinosTuristicos, id=id)
    if request.method == 'POST':
        form = DestinosTuristicosForm(request.POST, request.FILES, instance=destino)
        if form.is_valid():
            form.save()
            return redirect('listar_destinos')
