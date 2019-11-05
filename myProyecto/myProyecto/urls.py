"""myProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include #permite incluir ubicacion de archivo
from django.conf import settings #importar el archivo de configuracion del proyecto
from django.conf.urls.static import static #importar las direcciones estaticas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('cine.urls')),#redireccionar hacia archivo URLS
]
#al momento de cargar el archivo de url, se agrega la direccion statica del directorio MEDIA
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
