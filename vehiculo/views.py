from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import VehiculoForm
from .models import VehiculoModel
from django.contrib import messages

# Create your views here.
#Creación de vista inicio(Drilling Final, Parte 2)
def inicio(request):
           
    context ={}           
            
    return render(request, 'index.html', context)
#Creación del método input_models(Drilling Final, Parte 2)
def input_models(request):
    context = {}
    form = VehiculoForm(request.POST or None, request.FILES or None)
    #Sí el formulario está correcto se redirecciona a index
    if form.is_valid():
        form.save()
        messages.success(request, "El vehículo se agregado exitosamente")
        return HttpResponseRedirect('/')
    
    context['form'] = form
    return render(request,'add.html', context)