from django.urls import path
#Importación de las vistas
from .views import inicio

urlpatterns = [
   #Se agrega la url "index",(Drilling Final, parte 2)
   path('', inicio, name = 'index'),
  
]