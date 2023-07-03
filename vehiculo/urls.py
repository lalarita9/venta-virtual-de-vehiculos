from django.urls import path
#Importación de las vistas
from .views import inicio, input_models, navbar

urlpatterns = [
   #Se agrega la url "index",(Drilling Final, parte 2)
   path('', inicio, name = 'index'),
   #Se agrega la url "vehiculo/add",(Drilling Final, parte 2)
   path('vehiculo/add', input_models, name = 'vehiculo/add'),
   #Se agrega la url "navbar",(Drilling Final, parte 3)
   path('navbar/', navbar, name = 'navbar'),
   
  
]