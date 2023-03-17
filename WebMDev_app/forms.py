from django import forms
from django.forms import ModelForm
from .models import Producto


class Consultaform(forms.Form):
    nombre_form = forms.CharField(max_length=40)
    email = forms.EmailField()
    tema = forms.CharField(max_length=40)
    mensaje = forms.CharField(max_length=200)

class Compraform(forms.Form):
    username = forms.CharField(max_length=40)
    pago = forms.CharField(max_length=40)
    envio = forms.CharField(max_length=40)
    mensaje = forms.CharField(max_length=200)


"""class UpdateForm(UserCreationForm):
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    descripcion = forms.CharField(label='Descripcion', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=False)
    idnumber = forms.IntegerField(label="IDnumber", widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    tamaño = forms.CharField(label='Tamaño', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    precio = forms.IntegerField(label='Precio', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    valoracion = forms.CharField(label='Valorcion', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100, required=False)
    imagen = forms.ImageField(label="Imagen", widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)
    slug = forms.CharField(label='Slug', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
"""
class form_crearArticulo(ModelForm):
 class Meta:
        model=Producto
        fields=['nombre','descripcion','idnumber','tamaño','precio','valoracion','imagen','slug']


class form_modificarArticulo(ModelForm):
 class Meta:
        model=Producto
        fields=['nombre','descripcion','idnumber','tamaño','precio','valoracion','imagen','slug']
