from django.contrib import admin

from gestionTienda.models import *

class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","descripcion"]

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "tipo"]
    ordering = ["precio"]
    search_fields = ["nombre"]

class OrdenAdmin(admin.ModelAdmin):
    list_display = ["numero_orden","fecha"]
    list_filter = ["fecha"]
    date_hierarchy = "fecha"

class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nombre", "direccion","correo","telefono"]

class TipoEmpleadoAdmin(admin.ModelAdmin):
    list_display = ["nombre","descripcion"]

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "direccion","correo","telefono","sueldo","tipo"]

class SugerenciaAdmin(admin.ModelAdmin):
    list_display = ["nombre","descripcion"]

class DirectorioAdmin(admin.ModelAdmin):
    list_display = ["nombre", "direccion","correo","telefono","referencia"]


admin.site.register(TipoProducto, TipoProductoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Sugerencia, SugerenciaAdmin)
admin.site.register(Directorio, DirectorioAdmin)
admin.site.register(TipoEmpleado, TipoEmpleadoAdmin)
