from django import forms
from django.forms.widgets import Widget
#from django.db import forms
#from django-autocomplete-light import 
from .models import  Provincia, Programa, Localidad  #Farmacia,

class LocalidadActForm(forms.ModelForm):
    class Meta:

        model = Localidad
        
        fields = ['estado']

        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['estados'].widget.attrs.update({
                'class': 'form-control'
            })

        labels = {
            'estado' : 'estado de la localidad (Activar/Desactivar)'
        }

class LocalidadForm(forms.ModelForm):
    
    class Meta:
        # en la subclase Meta del ModelForm se indica el modelo al cual pertenece
        # el nombre de los campos que deben aparecer
        # y los widgets que sirven para darle estilos al formulario
        model = Localidad
        
        fields = ['id_localidad','descripcion','id_provincia_id']

        widgets = {
            'id_localidad': forms.TextInput(attrs={'class': 'form-control'}),
            'id_provincia_id.descripcion':forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'})

        }

        # def __init__(self,*args, **kwargs):
        #     super().__init__(*args, **kwargs)

        #     self.fields['id_provincia_id'].widget.attrs.update({
        #         'class': 'form-control'
        #     })

        labels = {
            'id_localidad': 'id de la localidad',
            'id_provincia_id.descripcion': 'provincia a la que pertenece',
            'descripcion': 'nombre de la localidad'
        }

#Formulario para agregar/actualizar un programa
class ProgramaActForm(forms.ModelForm):
    
    class Meta:

        model = Programa
        
        fields = ['estado']

        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['estados'].widget.attrs.update({
                'class': 'form-control'
            })

        labels = {
            'estado' : 'estado del programa (Activar/Desactivar)'
        }



#Formulario para crear farmacia
# class FarmaciaForm(forms.ModelForm):
#     class Meta:     
#         model = Farmacia
#         fields = ['fica_id', 'nombre', 'direccion']

#Formualrio para crear provincia
class ProvinciaForm(forms.ModelForm):
    class Meta:     
        model = Provincia
        fields = ['id_provincia', 'descripcion','estado']
        widgets={
            'id_provincia': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = { #permite definir una etiqueta personalizada para cada un de losa tributos
            'id' : 'id_provincia',
            'descripcion' : 'nombre de la provincia',
            'estado': 'estado'
        }

#Form para actualizar estado de una provincia
class ProvinciaActForm(forms.ModelForm):
    class Meta:     

        model = Provincia
        fields = ['estado']
        widgets={
            'estado': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = { #permite definir una etiqueta personalizada para cada un de losa tributos
            'estado': 'estado'
        }

#Formulario para agregar/actualizar un programa
class ProgramaForm(forms.ModelForm):
    
    class Meta:
        # en la subclase Meta del ModelForm se indica el modelo al cual pertenece
        # el nombre de los campos que deben aparecer
        # y los widgets que sirven para darle estilos al formulario
        model = Programa
        
        fields = ['programa','nombre','version','fecha_install']

        widgets = {
            'programa': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'version': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_install': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'programa': 'id del programa',
            'nombre': 'nombre del programa',
            'version': 'version del programa actual',
            'fecha_install': 'fecha de instalacion'
        }



class ProvinciaActForm(forms.ModelForm):
    
    class Meta:

        model = Provincia
        
        fields = ['estado']

        def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['estados'].widget.attrs.update({
                'class': 'form-control'
            })

        labels = {
            'estado' : 'estado de la provincia (Activar/Desactivar)'
        }

