"""Rutas globales: incluyen las cuatro aplicaciones del dominio."""
from django.urls import include, path

urlpatterns = [
    path('cuentas/', include('cuentas.urls')),
    path('catalogo/', include('catalogo.urls')),
    path('comunidades/', include('comunidades.urls')),
    path('actividades/', include('actividades.urls')),
]
