from django.contrib import admin

# Register your models here.

from .models import VehiculoModel

#Registro de App Vehiculo a sitio Django(Drilling Final, Parte 1)
admin.site.register(VehiculoModel)
