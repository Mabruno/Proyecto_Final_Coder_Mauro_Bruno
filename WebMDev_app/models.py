from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Producto(models.Model):
    nombre = models.CharField(blank=True, max_length=40, default='')
    descripcion = models.CharField(blank=True, max_length=100)
    idnumber = models.IntegerField(blank=True)
    tamaño = models.CharField(blank=True, max_length=10)
    precio = models.FloatField(default=0.0)
    valoracion = models.FloatField(blank=True, max_length=4, default=0.0)
    imagen = models.ImageField(blank=True, upload_to='media')
    slug = models.SlugField(blank=True, max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)

    def get_absolute_url(self):
        return reverse('productos', kwargs={'slug': self.slug})

    def __str__(self):
        return f"Nombre: {self.nombre} - Descripcion {self.descripcion} - IDnum {self.idnumber} - Precio {self.precio} - Valoracion {self.valoracion}"

    """def save(self, *args, **kwargs):
        # Generar un nombre único y aleatorio para la imagen
        if self.imagen:
            extension = self.imagen.name.split('.')[-1]
            self.imagen.name = f"{uuid.uuid4()}.{extension}"
        super().save(*args, **kwargs)"""

class Compra(models.Model):
    username = models.CharField(default='', max_length=40)
    pago = models.CharField(max_length=40)
    envio = models.CharField(max_length=40)
    mensaje = models.CharField(default=None, max_length=100)

    def __str__(self):
        return f"Usuario {self.username} - Pago {self.pago} -   Envio {self.envio} - Mensaje {self.mensaje}"

class Consulta(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    tema = models.CharField(max_length=40)
    mensaje = models.CharField(default='', max_length=200)

    def __str__(self):
        return f"Nombre: {self.nombre} - Email {self.email} -   Tema {self.tema} - Mensaje {self.mensaje}"

