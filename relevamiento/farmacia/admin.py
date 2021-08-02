from django.contrib import admin

from .models import Farmacia, Perfil, Usuario, Provincia, Localidad, Pc_Farmacia, Fcia #  se debe importar el modelo

# Register your models here.

admin.site.register(Farmacia) # se debe registrar el modelo en admin

# cambios para registrar los modelos en la vista de admin de django 
admin.site.register(Perfil)
admin.site.register(Usuario)
admin.site.register(Provincia)
admin.site.register(Localidad)
admin.site.register(Pc_Farmacia)
admin.site.register(Fcia)
