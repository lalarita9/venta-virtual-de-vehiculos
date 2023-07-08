from django.urls import path
#Importación de las vistas
from .views import indexView, input_models, navbar, registro_usuario, listar_vehiculo, \
      login_vehiculo, logout_vehiculo, editar_vehiculo, galeria_vehiculo

urlpatterns = [
   #Se agrega la url "index",(Drilling Final, parte 2)
   path('', indexView, name = 'index'),
   #Se agrega la url "vehiculo/add",(Drilling Final, parte 2)
   path('add/', input_models, name = 'add'),
   #Se agrega la url "navbar",(Drilling Final, parte 3)
   path('navbar/', navbar, name = 'navbar'),
   #Se agrega la url "registro",(Drilling Final, parte 4)
   path('registro/', registro_usuario, name = 'registro'),
   #Se agrega la url "login",(Drilling Final, parte 4)
   path('login/', login_vehiculo, name = 'login'),
   #Se indica vista "logout"(Drilling Final, parte 4)
   path('logout/', logout_vehiculo, name='logout'),
   #Se agrega la url "list",(Drilling Final, parte 4)
   path('list/', listar_vehiculo, name = 'list'),
   #Se agrega la url "modal",(Drilling Final, Extras)
   path('modal/<id>/', editar_vehiculo, name = 'modal'),
   #Se agrega la url "galeria",(Drilling Final, Extras)
   path('galeria/', galeria_vehiculo, name = 'galeria'),
  
]