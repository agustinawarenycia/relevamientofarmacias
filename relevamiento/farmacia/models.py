from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
program_status = [(0,"Desactivar"),(1,"Activar")]
# Clase que crea una tabla con los datos para los programas instalados
class Programa(models.Model):
    programa = models.IntegerField(primary_key=True)
    nombre = models.CharField("Nombre del Programa", max_length = 100, null = False, blank = False)
    version = models.CharField("Nombre del Programa", max_length = 100, null = False, blank = True)
    fecha_install = models.DateField(auto_now=False, auto_now_add=False,null = False, blank = False)
    estado = models.IntegerField(null=False,blank=False,choices=program_status,default=1)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'


# Tabla Perfil
class Perfil(models.Model):
    id_perfil = models.CharField("id_perfil", max_length = 256, null = False, blank = False,primary_key=True)
    descripcion = models.CharField("descripción perfil", max_length=256, null = False, blank = False)
    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

# Tabla Usuarios
class Usuario(models.Model):
    id_usuario = models.CharField("id_usuario", max_length=256, null = False, blank = False,primary_key=True)
    nombre = models.CharField("nombre", max_length= 256, null = False, blank = False)
    apellido = models.CharField("apellido", max_length= 256, null = False, blank = False)
    usuario = models.CharField("usuario", max_length= 256, null = False, blank = False)
    baja = models.BooleanField("usuario dado de baja si/no", default = True)
    id_perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE) # Clave foranea en Django
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

# Tabla de Provincias
provinica_status = [(0,"Desactivar"),(1,"activar")]
class Provincia(models.Model):
    id_provincia = models.IntegerField("id_provincia", null = False, blank = False, primary_key=True)
    descripcion = models.CharField("descripcion", max_length=256, null = False, blank = False)
    estado = models.IntegerField(null=False,blank=False,choices=provinica_status,default=1)
    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name = 'provincia'
        verbose_name_plural = 'provincias'

# Tabla localidad 
localidad_status=[(1,"Activar"),(0,"Desactivar")]
class Localidad(models.Model):
    id_localidad = models.IntegerField("Localidad", null = False, blank = False, primary_key=True)
    id_provincia_id = models.ForeignKey(Provincia, on_delete = models.CASCADE)
    descripcion = models.CharField("descripcion", max_length = 256, null = False, blank = False)
    estado = models.IntegerField(null=False, blank=False,choices=localidad_status,default=1)
    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name = 'localidad'
        verbose_name_plural = 'localidades'

# Tabla para Farmacias 
fcia_status =[(1,"Desactivar"),(0,"Activar")]
class Fcia(models.Model):
    nro_cliente  = models.IntegerField("Número de Cliente", default = 1 ,null = False, blank = False, primary_key=True)
    nombre_facia = models.CharField("nombre_farmacia", max_length = 256, null = True, blank  = True)
    id_localidad = models.ForeignKey(Localidad, on_delete = models.CASCADE)
    estado = models.IntegerField(null = False, blank = False, choices = fcia_status, default = 0) # en este caso el estado activo es = 0 inactivo = 1
    def __str__(self):
        return self.nombre_facia
    class Meta:
        verbose_name = 'Fcia'
        verbose_name_plural = 'Fcias'

# Tabla para las PC
class PC_detalles(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField("IP",max_length = 255, null = False, blank = False)
    nombre_pc = models.CharField("nombre_pc", max_length = 255, blank = True, null = True)
    id_AnyDesk = models.CharField("any_instalado", max_length = 255, blank = True, null = True)
    fecha_hora = models.DateTimeField("fecha y hora",auto_now_add=True ,null=True,blank=True)
    def __str__(self):
        return str(self.nombre_pc)
    class Meta:
        verbose_name = 'detalle'
        verbose_name_plural = 'detalles'

# Tabla para las Pcs de cada fcia
class Pc_Farmacia (models.Model):
    ip_publica = models.CharField("ip_publica", primary_key=True, max_length = 256, default="198.162.0.203")
    ip = models.CharField("IP", max_length = 256, null = False, blank = False)
    nro_cliente = models.ForeignKey(Fcia, on_delete=models.CASCADE, null=True)#cambio para filtro de computadoras por farmacia
    fecha_relevamiento = models.DateField("Fecha-Relevamiento", null = True, blank = True)#agregado    
    nombre_pc = models.CharField("nombre_pc", max_length = 256, blank = True, null = True)
    arquitectura_so = models.CharField("arquitectura_so", max_length = 256, blank = True, null = True)
    version_so = models.CharField("version",max_length=50,blank=True,null=True)#agregado
    tipo_maquina = models.CharField("tipo_maquina", max_length = 256, blank = True, null = True)
    procesador = models.CharField("procesador", max_length = 256, blank = True, null = True)
    cores_fisicos = models.IntegerField("cores_fisicos", null =True, blank = True)
    cores_totales = models.IntegerField("cores_totales", null = True, blank = True)
    RAM_tot = models.CharField("ram_total", max_length = 256, blank = True, null = True)
    RAM_usada = models.CharField("ram_usada", max_length = 256, blank = True, null = True)
    RAM_disponible = models.CharField("ram_disponible", max_length = 256, blank = True, null = True)
    RAM_procentaje_disponible = models.CharField("RAM_disponible", max_length=256, blank = True, null = True)#agregado
    espacio_tot_C = models.CharField("espacio_total_C", max_length = 256, blank = True, null = True)
    espacio_tot_D = models.CharField("espacio_total_D", max_length = 256, blank = True, null = True)
    espacio_usado_C = models.CharField("espacio_usado_C", max_length = 256, blank = True, null = True)
    espacio_usado_D = models.CharField("espacio_usado_D", max_length = 256, blank = True, null = True)
    espacio_disponible_C = models.CharField("espacio_disponible_C", max_length = 256, blank = True, null = True)
    espacio_disponible_D = models.CharField("espacio_disponible_D", max_length = 256, blank = True, null = True)
    procentaje_disponible_C = models.CharField("porcentaje_disponible_C", max_length = 256, null = True, blank = True)#agregado
    procentaje_disponible_D = models.CharField("porcentaje_disponible_D", max_length = 256, null = True, blank = True)#agregado
    AnyDesk_instalado = models.CharField("any_instalado", max_length = 256, blank = True, null = True)
    id_AnyDesk = models.CharField("any_instalado", max_length = 256, blank = True, null = True)
    def __str__(self):
        return str(self.nombre_pc)
    class Meta:
        verbose_name = 'computadora'
        verbose_name_plural = 'computadoras'

# Tabla para los programas instalados en cada pc
class Programas_instalados(models.Model):
    programa_id = models.AutoField(primary_key=True)
    pc = models.ForeignKey(Pc_Farmacia, on_delete=models.CASCADE, null=True)
    nombre = models.CharField("Nombre del Programa", max_length = 100, null = False, blank = False)
    version = models.CharField("Nombre del Programa", max_length = 100, null = False, blank = True)
    fecha_install = models.CharField("Fecha de isntalación", max_length = 256, null = False, blank = False)
    def __str__(self):
        return self.nombre    
    class Meta:
        verbose_name = 'Programa_pc'
        verbose_name_plural = 'Programas_pc'

# Tabla para guardar los datos del relevamiento
class Relevamiento(models.Model):
    id =  models.AutoField(primary_key=True)
    farmacia = models.ForeignKey(Fcia, on_delete=models.CASCADE, null=True)#cambio para filtro de computadoras por farmacia
    fecha_relevamiento = models.DateTimeField("Fecha-Relevamiento", null = True, blank = True)#agregado    
    ip = models.CharField("IP", max_length = 256, null = False, blank = False)
    nombre_pc = models.CharField("nombre_pc", max_length = 256, blank = True, null = True)
    ip_publica = models.CharField("ip_publica", max_length = 256, blank = True, null = True)
    arquitectura_so = models.CharField("arquitectura_so", max_length = 256, blank = True, null = True)
    version_so = models.CharField("version",max_length=50,blank=True,null=True)#agregado
    tipo_maquina = models.CharField("tipo_maquina", max_length = 256, blank = True, null = True)
    procesador = models.CharField("procesador", max_length = 256, blank = True, null = True)
    cores_fisicos = models.IntegerField("cores_fisicos", null =True, blank = True)
    cores_totales = models.IntegerField("cores_totales", null = True, blank = True)
    RAM_tot = models.CharField("ram_total", max_length = 256, blank = True, null = True)
    RAM_usada = models.CharField("ram_usada", max_length = 256, blank = True, null = True)
    RAM_disponible = models.CharField("ram_disponible", max_length = 256, blank = True, null = True)
    RAM_procentaje_disponible = models.CharField("RAM_disponible", max_length=256, blank = True, null = True)#agregado
    espacio_tot_C = models.CharField("espacio_total_C", max_length = 256, blank = True, null = True)
    espacio_tot_D = models.CharField("espacio_total_D", max_length = 256, blank = True, null = True)
    espacio_usado_C = models.CharField("espacio_usado_C", max_length = 256, blank = True, null = True)
    espacio_usado_D = models.CharField("espacio_usado_D", max_length = 256, blank = True, null = True)
    espacio_disponible_C = models.CharField("espacio_disponible_C", max_length = 256, blank = True, null = True)
    espacio_disponible_D = models.CharField("espacio_disponible_D", max_length = 256, blank = True, null = True)
    procentaje_disponible_C = models.CharField("porcentaje_disponible_C", max_length = 256, null = True, blank = True)#agregado
    procentaje_disponible_D = models.CharField("porcentaje_disponible_D", max_length = 256, null = True, blank = True)#agregado
    AnyDesk_instalado = models.CharField("any_instalado", max_length = 256, blank = True, null = True)
    id_AnyDesk = models.CharField("any_instalado", max_length = 256, blank = True, null = True)
    def __str__(self):
        return str(self.nombre_pc)
    class Meta:
        verbose_name = 'relevamiento'
        verbose_name_plural = 'relevamientos'

# Tablas de prueba
class probando_programas(models.Model):
    id =  models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre del Programa", max_length = 100, null = False, blank = False)
    version = models.CharField("Nombre del Programa", max_length = 100, null = False, blank = True)
    fecha_install = models.CharField("fecha install", max_length = 100, null = False, blank = True)
    pc = models.ForeignKey(Pc_Farmacia,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.nombre)
    class Meta:
        verbose_name = 'programa-guardado'
        verbose_name_plural = 'programas-guardados'

class Cantidad_Programas(models.Model):
    id = models.IntegerField(primary_key=True)
    tabla_programas = models.ForeignKey(Pc_Farmacia,on_delete=models.CASCADE,null=True)
    cantidad = models.IntegerField("cantidad de programas", null=False, blank=False)
    class Meta:
        verbose_name = 'cantidad_programas' 


#-------------------------------MODELO PARA USUARIOS PREDEFINIDOS DE DJANGO---------------------------------


# Tabla de Usuarios de Django
class MainUser(AbstractBaseUser):
    usuario = models.CharField("Nombre de Usuario", unique = True, max_length = 100)
    nombre = models.CharField("Nombres", max_length = 256, null = True, blank = True)
    apellido = models.CharField("Apellidos", max_length = 256, null = True, blank = True)
    usuario_activo = models.BooleanField(default = True)
    usuario_admin = models.BooleanField(default = False)

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['usuario','nombre','apellido']
    
    def __str__(self):
        return f'Usuario: {self.usuario}'

    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app,label):
        return True

    @property
    def is_staff(self):
        return self.usuario_admin


class UsuarioManager(BaseUserManager):
    def create_user(self,usuario,nombre,apellido,password=None):
        if not usuario:
            raise ValueError('Nombre de usuario obligatorio')
        usuario = self.model(
            usuario = usuario,
            nombre=nombre,
            apellido=apellido
        )
        usuario.set_password(password)
        usuario.save()
        return usuario
    def create_super_user(self,usuario,nombre,apellido,password):
        usuario = self.create_user(
            usuario = usuario,
            nombre=nombre,
            apellido=apellido,
            password=password
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario