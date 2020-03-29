from django.contrib import admin
from BaseDatos.models import Persona,Perfil,Permiso,Acceso,Articulo,Permisos_Acceso,Estado_Sistema,Prestamo,Multa,Sesion
# Register your models here.
admin.site.register(Persona)
admin.site.register(Perfil)
admin.site.register(Permiso)
admin.site.register(Acceso)
admin.site.register(Articulo)
admin.site.register(Permisos_Acceso)
admin.site.register(Estado_Sistema)
admin.site.register(Prestamo)
admin.site.register(Multa)
admin.site.register(Sesion)

