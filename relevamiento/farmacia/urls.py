# es necesario el url patterns  #URL CRUD
#from relevamiento.farmacia.models import Provincia
from django.urls import path

from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from . import views
# from django.urls import reverse_lazy
from .views import (
    #HomeView,
    ListarFciasNav,
    VistaPrueba,
    filtro,
    vista_PC,
    ActivarLocalidad,
    #ProbandoLista,
    AgregarLoc,
    ListarLocDes,
    #ActualizarProvAct,
    ActivarProvincia,
    ActivarPrograma,
    ListarProvDesactivadas,
    ListarProgramas,
    AgregarPrograma,
    EliminarPrograma,
    Actualizarprograma,
    EliminarProv,
    ActualizarProv,
    CrearProv, 
    ListarProv,  
    ListarFcias,   
    ListarLoc,
    ListarProgDesactivados,
    vista_PC,
    vista_programas,
    BuscarFcia,
    ListadoProgramasActivos,
    total_prog,
    vista_PC,
    vista_especifica,
    #ListarProvNuevo,
   # load_cities
    
)

urlpatterns = [
    path('activar_localidad/<int:pk>', login_required(ActivarLocalidad.as_view()), name ="activar_localidad"),

    #-------------------------------- LOGIN --------------------------------
    path('lista_localidades/', login_required(ListarLoc.as_view()), name ="lista_localidades"),
    path('agregar_localidad/',login_required(AgregarLoc.as_view()),name = "agregar_localidad"),
    #-------------------------- Ruteo de CRUD  Para Programas --------------------------
    path('lista_programas/',login_required(ListarProgramas.as_view()), name = 'lista_programas'),
    path('agregar_programas/',login_required(AgregarPrograma.as_view()), name = 'agregar_programas'),
    path('eliminar_programa/<int:pk>',login_required(EliminarPrograma.as_view()), name  = 'eliminar_programa'),
    path('actualizar_programa/<int:pk>',login_required(Actualizarprograma.as_view()), name  = 'actualizar_programa'),
    path('activar_programa/<int:pk>', login_required(ActivarPrograma.as_view()),name = 'activar_programa'),

    path('activar_provincia/<int:pk>',login_required(ActivarProvincia.as_view()),name  = 'activar_provincia'),
    path('listar_provincias/', login_required(ListarProv.as_view()), name  = 'listar_provincias'),
    path('lista_prov_desactivadas/',login_required(ListarProvDesactivadas.as_view()),name = 'lista_prov_desactivadas'),
    path('agregar_prov/', CrearProv.as_view(), name  = 'agregar_prov'),
    path('eliminar_prov/<int:pk>', EliminarProv.as_view(), name  = 'eliminar_prov'),
    path('actualizar_prov/<int:pk>', ActualizarProv.as_view(), name  = 'actualizar_prov'),
    path('lista_farmacias/', login_required(ListarFcias.as_view()), name ="lista_farmacias"),
    path('lista_programas_desactivados/', login_required(ListarProgDesactivados.as_view()), name ="lista_programas_desactivados"),
    path('localidades_desactivadas/',login_required(ListarLocDes.as_view()),name = 'localidades_desactivadas'),

    #path('listar_farmacias_2/',login_required(ProbandoLista.as_view()), name = 'listar_farmacias_2'),
    path('especificacion_pc/',login_required(vista_PC.as_view()), name = 'especificacion_pc'),
    path('programas/',login_required(vista_programas.as_view(), ListadoProgramasActivos.as_view(), views.total_prog), name = 'programas'),
    path('buscar_fcia/',login_required(BuscarFcia.as_view()), name = 'buscar_fcia'),
    path('lista_farmacias_nav/',login_required(ListarFciasNav.as_view()), name = 'lista_farmacias_nav'),
    
    path('especif_pc/',login_required(vista_especifica.as_view()), name = 'especif_pc'),
    
    
    #path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),

    path('main/',login_required(VistaPrueba.as_view()), name = 'main'),
    path('data-json/', filtro.as_view(), name='data-json'),

   
] 
