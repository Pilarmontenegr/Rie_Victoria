from django.contrib import admin
from appRieVictoria.models import Articulos,Clientes,compraProd,Compras,Empleados,ventaProd,Ventas,Proveedores,TipoPrenda,tipoFactura

class ventaAdmin(admin.ModelAdmin):
    list_display= ("idEmpleado", "idClientes", "fecha", "tipoFactura")

admin.site.register(Articulos)
admin.site.register(Clientes)
admin.site.register(compraProd)
admin.site.register(Compras)
admin.site.register(Empleados)
admin.site.register(ventaProd)
admin.site.register(Ventas,ventaAdmin)
admin.site.register(Proveedores)
admin.site.register(TipoPrenda)
admin.site.register(tipoFactura)

