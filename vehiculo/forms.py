# importar la librería estándar de Django Forms
from django import forms
from .models import VehiculoModel

#Creación ModelForm (Drilling Final, parte 1 y 2)
class VehiculoForm(forms.ModelForm): 
    #Específica el nombre del modelo a usar
    class Meta: 
        model = VehiculoModel 
        fields = "__all__" #para que se puedan usar todos