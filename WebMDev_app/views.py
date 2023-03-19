from WebMDev_app.models import Producto, Consulta, Compra
from WebMDev_app.forms import Consultaform, Compraform, form_crearArticulo, UserCreationForm_app
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound,Http404, HttpResponse


def inicio(request):
    return render(request, 'inicio.html')

def enobra(request):
    return render(request, 'enobra.html')



#--->MODULO DE PRODUCTOS<---

#--Class Based Views--

class Productoslist(ListView):

    model = Producto
    template_name = 'productos.html'


class Productosdetail(DetailView):

    model = Producto
    template_name = "productos_detail.html"
    context_object_name = "producto"
    slug_field = "slug"


class Productosadmin(LoginRequiredMixin, ListView):

    model = Producto
    template_name = "productos_admin.html"

class Productosofer(ListView):

    model = Producto
    template_name = 'ofertas.html'

class Productosofer(ListView):

    model = Producto
    template_name = 'ofertas.html'

#--Def Method Views-

@login_required
def Productoscreacion(request):
    if request.method == 'GET':
        return render(request, 'productos_create.html', {'form': form_crearArticulo()})
    else:
        formulario = form_crearArticulo(request.POST, request.FILES)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            nuevoArticulo = Producto()
            nuevoArticulo.userName = request.user.username
            nuevoArticulo.precio = informacion['precio']
            nuevoArticulo.nombre = informacion['nombre']
            nuevoArticulo.idnumber = informacion['idnumber']
            nuevoArticulo.tamaño = informacion['tamaño']
            nuevoArticulo.valoracion = informacion['valoracion']
            nuevoArticulo.descripcion = informacion['descripcion']
            nuevoArticulo.slug = informacion['slug']

            if request.FILES.get('imagen'):
                nuevoArticulo.imagen = request.FILES['imagen']

            nuevoArticulo.save()
            return redirect('productos')
        else:
            return render(request, 'productos_create.html', {'form': formulario})


@login_required
def Productosdelete(request, slug):
    try:
        producto = get_object_or_404(Producto, slug=slug)
    except Http404:
        return HttpResponseNotFound(print(slug), '<h1>Producto inexistente</h1>')
    producto.delete()
    return redirect(reverse('productos'))


# Modificar Producto - GET request processing
@login_required
def modificarproducto(request, slug):

    if request.method == 'GET':
        try:
            producto = get_object_or_404(Producto, slug=slug)
        except Http404:
            return HttpResponseNotFound(print(slug), '<h1>Producto inexistente</h1>')

        formulario = form_crearArticulo(instance=producto)
        return render(request, 'productos_modificar.html', {'form': formulario})

# Modificar producto  - POST request processing
@login_required()
def modificadoproducto(request):

        formulario = form_crearArticulo(request.POST, request.FILES)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            articulo_existente = get_object_or_404(Producto, slug=informacion['slug'])
            articulo_existente.precio = informacion['precio']
            articulo_existente.nombre = informacion['nombre']
            articulo_existente.tamaño = informacion['tamaño']
            articulo_existente.valoracion = informacion['valoracion']
            articulo_existente.descripcion = informacion['descripcion']
            articulo_existente.slug = informacion['slug']

            if request.FILES.get('imagen'):
                articulo_existente.imagen = request.FILES['imagen']

            articulo_existente.save()

        return redirect('inicio')


#--->MODULO DE USUARIOS<---
#---->LOGIN - REGISTRO DE  USUARIO<-----

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm_app()
        return render(request, 'registro.html', {
            'form': form
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                form = UserCreationForm_app(request.POST)
                if form.is_valid():
                    username = form.cleaned_data.get('username')
                    email = form.cleaned_data.get('email')
                    password = form.cleaned_data.get('password1')
                    user = User.objects.create_user(username=username, email=email, password=password)
                    login(request, user)
                    return redirect('inicio')

            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })

        return render(request, 'registro.html', {
            'form': UserCreationForm_app,
            'error': 'Las contraseñas no coinciden'
        })


def signout(request):
    logout(request)
    return redirect('inicio')


def signin(request):
    if request.method == "GET":
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
            'form': AuthenticationForm,
            'error': 'Usuario o contraseña incorrectos'
        })
        else:
            login(request, user)
            return redirect('inicio')




#--->MODULO DE CONTACTO<---

def contacto(request):

    if request.method == 'POST':
        formulario_consulta = Consultaform(request.POST)

        if formulario_consulta.is_valid():
            informacion = formulario_consulta.cleaned_data
            consulta = Consulta(nombre=informacion['nombre_form'], email=informacion['email'],
                                  tema=informacion['tema'], mensaje=informacion['mensaje'])
            consulta.save()

            return render(request, 'contacto.html')

    else:
        formulario_consulta = Consultaform()

    return render(request, 'contacto.html', {'formulario_consulta': formulario_consulta})




#--->MODULO DE COMPRA---

@login_required()
def compra(request):

    if request.method == 'POST':
        formulario_compra = Compraform(request.POST)

        if formulario_compra.is_valid():

            informacion = formulario_compra.cleaned_data

            compra = Compra(username=informacion['username'], pago=informacion['pago'],
                                  envio=informacion['envio'], mensaje=informacion['mensaje'])
            compra.save()

            return render(request, "inicio.html", {"mensaje": f"Su mensaje fue enviado"})

        else:

            print(formulario_compra.errors)

    else:

        formulario_compra = Compraform()


    return render(request, 'compra.html', {'formulario_compra': formulario_compra})



def nosotros(request):
    return render(request, 'nosotros.html')


