from django.shortcuts import render
from .models import Categoria,Pelicula #importar los modelos de Categoria y Pelicula
# para trabajar con usuarios debemos importar
# modelo de tablas de user
from django.contrib.auth.models import User
# importar libreria de autentificacion
from  django.contrib.auth import authenticate,logout,login as login_autent
# agregar un "decorator" para impedir ingresar a las paginas si no esta logeado
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    return render(request,'core/index.html')

@login_required(login_url='/login/')
def galeria(request):
    pelis=Pelicula.objects.all()    
    return render(request,'core/galeria.html',{'peliculas':pelis})

def login(request):
    if request.POST:
        usuario=request.POST.get("txtUsuario")
        password=request.POST.get("txtPass")
        us=authenticate(request,username=usuario,password=password)
        msg=''
        if us is not None and us.is_active:
            login_autent(request,us)#autentificacion de login
            return render(request,'core/index.html')
        else:
            return render(request,'core/login.html')

    return render(request,'core/login.html')

#permite cerrar session
def cerrar_session(request):
    logout(request)
    return render(request,'core/login.html')

def login_acceso(request):
    if request.POST:
        usuario=request.POST.get("txtUsuario")
        password=request.POST.get("txtPass")
        us=authenticate(request,username=usuario,password=password)
        msg=''
        if us is not None and us.is_active:
            login_autent(request,us)#autentificacion de login
            return render(request,'core/index.html')
        else:
            return render(request,'core/login.html')

@login_required(login_url='/login/')
def carro_compras(request,id):
    lista=request.session.get('carrito','')
    lista=lista+str(id)+":1 ,"
    pelis=Pelicula.objects.all()
    request.session["carrito"]=lista
    arr=lista.split(',') 
    return render(request,'core/galeria.html',{'peliculas':pelis,'lista':arr})

@login_required(login_url='/login/')
def eliminar_pelicula(request,id):
    peli=Pelicula.objects.get(name=id)
    mensaje=''
    try:
        peli.delete()
        mensaje='Pelicula Eliminada'
    except:
        mensaje='Problemas de Eliminacion Pelicula'

    pelis=Pelicula.objects.all()
    return render(request,'core/galeria.html',{'peliculas':pelis,'msg':mensaje})

@login_required(login_url='/login/')
def formulario(request):
    catego=Categoria.objects.all()# select * from categoria
    if request.POST:
        titulo=request.POST.get("txtTitulo")
        duracion=request.POST.get("txtDuracion")
        precio=request.POST.get("txtPrecio")
        descripcion=request.POST.get("txtDescripcion")
        categoria=request.POST.get("cboCategoria")
        #ubicamos de la tabla (modelo) Categoria el reg. con "name" igual al valor
        #recuperado del combo "cboCategoria"
        obj_categoria=Categoria.objects.get(name=categoria)
        imagen=request.FILES.get("imagen")
        #crear una instancia del modelo Pelicula
        pelicula=Pelicula(
            name=titulo,
            duracion=duracion,
            precio=precio,
            descripcion=descripcion,
            categoria=obj_categoria,
            imagen=imagen
        )
        pelicula.save() #se graba el contenido del objeto pelicula
        return render(request,'core/formulario.html',{'categorias':catego,'msg':'grabo'})
    return render(request,'core/formulario.html',{'categorias':catego})

@login_required(login_url='/login/')
def formulario2(request):
    return render(request,'core/formulario2.html')

@login_required(login_url='/login/')
def quienessomos(request):
    return render(request,'core/quienes_somos.html')
