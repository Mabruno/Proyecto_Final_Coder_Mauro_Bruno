from django.contrib import admin
from .models import Producto, Compra, Consulta

admin.site.register(Producto)
admin.site.register(Consulta)
admin.site.register(Compra)
