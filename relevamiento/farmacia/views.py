#from relevamiento.farmacia.models import Farmacia
#from relevamiento.settings import SWEETIFY_SWEETALERT_LIBRARY
from django.http.response import HttpResponse
from django.views.generic.base import  View
from django.views.generic.edit import CreateView
from .forms import (FciaActForm,
                    LocalidadForm, 
                    ProgramaForm, 
                    ProvinciaForm, 
                    ProgramaActForm, 
                    ProvinciaActForm,
                    LocalidadActForm,
                    FciaForm)
from .models import (Pc_Farmacia,
                    PC_detalles,
                    Fcia, 
                    Programa, 
                    Provincia, 
                    Localidad,
                    Programas_instalados,
                    Cantidad_Programas,
                    probando_programas)

 #import de las vistas basadas en clases
from django.views.generic import (TemplateView, #Vista basada en clase para renderizar una página estática simple 
                                ListView, #Vista basada en clase para renderizar un template de listas
                                UpdateView, #Vista basada en clase para renderizar un template de Actualizacón
                                CreateView, #Vista basada en clase para renderizar un template de Creacion
                                DeleteView) #Vista basada en clase para renderizar un template de Borrado
from django.urls import reverse_lazy

# Vista que renderiza el login
class Login(TemplateView):
    template_name = 'farmacia/login.html' # indicar la ruta desde la raiz sin especificar esta misma
#-------------------------- CRUD de ciudades --------------------------
#------------------vista para listar las localidades
class ListarLoc(ListView):
    model = Localidad
    template_name = 'farmacia/listar_localidades.html'
    context_object_name = 'localidad'
    
    # Redefinicion del metodo get_queryset para realizar la consulta de filtro de ciudad por provincia
    def get_queryset(self):
        qs = Localidad.objects.select_related('id_provincia_id').all() # qs igual
        provincia = self.request.GET.get("lang")
        if provincia:
            qs = qs.filter(id_provincia_id = provincia)
        return qs

# Vista basada en clase para listar los datos de las localidades desactivadas
class ListarLocDes(ListView):
    model = Localidad
    template_name = 'farmacia/localidades_desactivadas.html'
    context_object_name = 'localidad'
    queryset = Localidad.objects.all()

class AgregarLoc(CreateView):
    model = Localidad
    template_name = 'farmacia/agregar_localidad.html'
    form_class = LocalidadForm
    success_url = reverse_lazy('farmacia:lista_localidades') 

class ActivarLocalidad(UpdateView):
    model = Localidad
    template_name = 'farmacia/agregar_localidad.html'
    form_class = LocalidadActForm
    success_url = reverse_lazy('farmacia:lista_localidades')

#--------------------------FIN CRUD de ciudades --------------------------

#-------------------------- CRUD de programas --------------------------

# Vista basada en clase para listar los programas eliminados/desactivados
class ListarProgDesactivados(ListView):
    model = Programa
    template_name = 'farmacia/lista_programas_desactivados.html'
    context_object_name = 'programas'
    queryset = Programa.objects.all()

# Vista basada en clase para listar programas (EN PROCESO)
class ListarProgramas(ListView):
    model = Programa
    template_name = 'farmacia/lista_programas.html'
    context_object_name = 'programas'
    queryset = Programa.objects.all() # esta funcion devuelve una consulta que retorna todas las filas de la tabla programa

# Vista basada en clase para agregar un nuevo programa
class AgregarPrograma(CreateView):
    model = Programa
    template_name = 'farmacia/agregar_programa.html'
    form_class = ProgramaForm
    success_url = reverse_lazy('farmacia:lista_programas')

# Vista basada en clase para eliminar completamente un objeto de la base de datos 
class EliminarPrograma(DeleteView):
    model = Programa
    success_url =  reverse_lazy('farmacia:lista_programas_desactivados')

#Vista basada en clase para actualizar un programa
class Actualizarprograma(UpdateView):

    model = Programa
    template_name = 'farmacia/agregar_programa.html'
    form_class = ProgramaForm
    success_url = reverse_lazy('farmacia:lista_programas')

class ActivarPrograma(UpdateView):
    model = Programa
    template_name = 'farmacia/agregar_programa.html'
    form_class = ProgramaActForm
    success_url = reverse_lazy('farmacia:lista_programas')


class ActivarPrograma(UpdateView):
    model = Programa
    template_name = 'farmacia/agregar_programa.html'
    form_class = ProgramaActForm
    success_url = reverse_lazy('farmacia:lista_programas')
#-------------------------- FIN CRUD de programas --------------------------
    
#--------------------------  CRUD de Provincias --------------------------

class ActivarProvincia(UpdateView):
    model = Provincia
    template_name = 'farmacia/agregar_prov.html'
    form_class = ProvinciaActForm
    success_url = reverse_lazy('farmacia:listar_provincias')

# Vista basada en clase para listar los datos de las Provincias
class ListarProv(ListView):
    model = Provincia
    template_name = 'farmacia/listar_provincias.html'
    context_object_name = 'provincias' #objeto para recorrer la tabla
    queryset = Provincia.objects.all()

#Vista basada en clase para listar las Provincias Desactivadas
class ListarProvDesactivadas(ListView):
    model = Provincia
    template_name = 'farmacia/lista_prov_desactivadas.html'
    context_object_name = 'provincias'
    queryset = Provincia.objects.all() #consulta a la abse de datos

# Vista basada en clase para agregar una provincia
class CrearProv(CreateView):
    model = Provincia
    template_name = 'farmacia/agregar_prov.html'
    form_class = ProvinciaForm
    success_url = reverse_lazy('farmacia:listar_provincias')

#Vista basada en clase para actualizar una provincia
class ActualizarProv(UpdateView):
    model = Provincia
    template_name = 'farmacia/agregar_prov.html'
    form_class = ProvinciaForm
    success_url = reverse_lazy('farmacia:listar_provincias')

# vista basada en clase que  hace una eliminación directa de los registros de la base de datos
class EliminarProv(DeleteView):
    model = Provincia
    success_url = (reverse_lazy('farmacia:listar_provincias'))   

# Codigo para editar una provincia (repetido revisar)
class EditarProvincia(UpdateView):  
    model = Provincia
    template_name = 'farmacia/agregar_prov.html'
    form_class = ProvinciaForm
    success_url = reverse_lazy('farmacia:listar_provincias')

#-------------------------- FIN CRUD de Provincias --------------------------
#qs = Pc_Farmacia.objects.select_related('farmacia').all()
# Vista basada en clase para listar las farmacias
class ListarFcias(ListView):
    model = Fcia
    template_name = 'farmacia/listar_farmacias.html'
    context_object_name = 'fcias'

    # Redefinicion del metodo get_queryset para realizar la consulta de filtro de farmacia por ciudad
    def get_queryset(self):
        qs = Fcia.objects.select_related('id_localidad').all() # trago todas las farmacias
        farmacia = self.request.GET.get("lang")
        
        
        
        if farmacia:
            qs = qs.filter(id_localidad = farmacia)
        return qs

#----------------vista para listar varios modelos a la vez en un mismo template------------
class Inicio(ListView):
    template_name = 'index.html'
    model = Provincia
    second_model = Localidad
    third_model = Fcia

    def get_context_data(self, *args, **kwargs): 
        provincias = Provincia.objects.all()
        localidades = Localidad.objects.all()
        farmacias = Fcia.objects.all()
        return {'provincias': provincias, 'localidades': localidades, 'farmacias':farmacias}
    

class vista_PC(ListView):
    model = Pc_Farmacia
    second_model = Fcia
    template_name = 'farmacia/especificacion_pc.html'
    context_object_name = 'computadoras'
    def get_queryset(self):
        qs = Pc_Farmacia.objects.select_related('nro_cliente').all() # qs igual
        farmacia = self.request.GET.get("lang")
        if farmacia:
            qs = qs.filter(nro_cliente=farmacia)
        return qs

class vista_programas(ListView):
    model = Programas_instalados
    second_model = Pc_Farmacia
    template_name = 'farmacia/programas_pc.html'
    context_object_name = 'programas'
    queryset = Programas_instalados.objects.all()

    def get_queryset(self):
        qs = Programas_instalados.objects.select_related('pc_id').all() # qs igual
        pc = self.request.GET.get("lang")
        if pc:
            qs = qs.filter(pc_id=pc)
        return qs


def imagen():
    with open("mensaje.jpg", "rb") as f:
        return HttpResponse(f.read(), content_type="static/img/")
    
class BuscarFcia(ListView):
    model = Fcia
    template_name = 'farmacia/listar_farmacias.html'
    context_object_name = 'fcias'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Fcia.objects.filter(nro_cliente__icontains=query) or Fcia.objects.filter(nombre_facia__icontains=query) or Fcia.objects.filter(id_localidad__descripcion__icontains=query) or Fcia.objects.filter(id_localidad__id_provincia_id__descripcion__icontains=query) 

class ListarFciasNav(ListView):
    model = Fcia
    template_name = 'farmacia/lista_farmacias_nav.html'
    context_object_name = 'fcias'
    # Redefinicion del metodo get_queryset para realizar la consulta de filtro de farmacia por ciudad
    def get_queryset(self):
        qs = Fcia.objects.select_related('id_localidad').all() # trago todas las farmacias
        farmacia = self.request.GET.get("lang")
        #Cambair esta parte del codigo para que compare el id de provincia con el de localidad y desp con el de farmacia
        if farmacia:
            qs = qs.filter(id_localidad = farmacia)
        return qs

class probando_tabla(ListView):
    model = probando_programas
    template_name = 'farmacia/probando_tabla.html'
    context_object_name = 'programs'
    queryset = probando_programas.objects.all()

class vista_especifica(ListView):
    model = Pc_Farmacia
    template_name = 'farmacia/especif_pc.html'
    context_object_name = 'computadoras'
    queryset = Pc_Farmacia.objects.all()
    

    def get_queryset(self):
        qs = Pc_Farmacia.objects.select_related('nro_cliente').all() # qs igual
        farmacia = self.request.GET.get("lang")
        if farmacia:
            qs = qs.filter(nro_cliente = farmacia)
        return qs

class ProgramasInstalados(ListView):
    model = Programas_instalados
    second_model = Cantidad_Programas
    template_name = 'farmacia/programas_instalados.html'
    
    context_object_name = 'programs'

    def get_queryset(self):
        qs = Programas_instalados.objects.all() # qs igual
        programa = self.request.GET.get("lang")
        if programa:
            qs = qs.filter(pc_id = programa)
        return qs

from .models import Pc_Farmacia
from django.core import serializers
from django.http import JsonResponse, request

class PruebaModel(View):
    
    def get(self, request):
        qs = Pc_Farmacia.objects.all()
    
        data  = serializers.serialize('json', qs)
        return JsonResponse({'data':data}, safe=False)    

class probando_tabla_2(TemplateView):
    template_name = 'farmacia/probando_tabla_2.html'

class Crear_usuario(TemplateView):
    template_name = 'farmacia/agregar_usuario.html'

#---------------------------CRUD FCIAS---------------------------------------------------------------------------
# Agregar Fcia
class add_fcia(CreateView):
    template_name = 'farmacia/crud_fcias/agregar_fcia.html'
    model = Fcia
    success_url = reverse_lazy('farmacia:lista_farmacias_nav')
    form_class = FciaForm
    



# Listar Fcias Inactivas
class list_inactive_fcias(ListView):
    template_name = 'farmacia/crud_fcias/lista_fcias_desactivadas.html'
    model = Fcia
    context_object_name = 'fcias'

# Actualizar Estado Fcia
class ActivarFcia(UpdateView):
    model = Fcia
    template_name = 'farmacia/crud_fcias/agregar_fcia.html'
    form_class = FciaActForm
    success_url = reverse_lazy('farmacia:lista_farmacias_nav')

# Borrar Fcia
class delete_fcia(DeleteView):
    model = Fcia
    success_url = (reverse_lazy('farmacia:lista_farmacias_nav'))