from django.contrib import admin

from CRUD1.models import Usuario
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido","nombre_usuario","email","tfno")

admin.site.register(Usuario,UsuarioAdmin)
