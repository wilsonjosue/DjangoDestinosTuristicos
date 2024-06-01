"""
URL configuration for sistema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# sistema/urls.py
from django.contrib import admin
from django.urls import path
from django.urls import path, include
#Importa el objeto settings de Django, que contiene las configuraciones del proyecto, relacionadas con archivos estáticos y de medios.
from django.conf import settings 
#Importa la función static que se utiliza para servir archivos estáticos y de medios durante el desarrollo.
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('travello.urls')),
    path('destinos/', include('travello.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#Añade una nueva ruta a urlpatterns para servir archivos de medios.