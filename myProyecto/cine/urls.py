from django.contrib import admin
from django.urls import path
from .views import home,galeria,formulario,formulario2,quienessomos,eliminar_pelicula,login,carro_compras,cerrar_session

urlpatterns = [
    path('',home,name='HOME'),
    path('galeria/',galeria,name='GALE'),
    path('formulario/',formulario,name='FORMU'),
    path('formulario2/',formulario2,name='FORMU2'),
    path('quienes_somos/',quienessomos,name='QUIEN'),
    path('eliminar_pelicula/<id>/',eliminar_pelicula,name='ELIMINAR'),
    path('agregar_carro/<id>/',carro_compras,name='AGREGAR_CARRO'),
    path('login/',login,name='LOGIN'),
    path('cerrar_session/',cerrar_session,name='LOGOUT'),
]