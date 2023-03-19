from WebMDev_app import views
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('enobra/', views.enobra, name='enobra'),
    path('contacto/', views.contacto, name='contacto'),
    path('compra/', views.compra, name='compra'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('ofertas/', views.Productosofer.as_view(), name='ofertas'),
    path('productos/', views.Productoslist.as_view(), name='productos'),
    path('login/', views.signin, name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.signup, name='register'),
    path('productos/admin/<slug:slug>/', views.Productosdetail.as_view(), name='productos'),
    path('productos/delete/<slug:slug>', views.Productosdelete, name='delete'),
    path('productos/admin/', views.Productosadmin.as_view(), name='admin'),
    path('productos_create/', views.Productoscreacion, name="crearArticulo"),
    path('productos/modificar/<slug:slug>', views.modificarproducto, name='modificar'),
    path('productos_modificado/', views.modificadoproducto, name='modificado'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)