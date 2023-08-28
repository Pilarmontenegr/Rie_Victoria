from django.contrib import admin
from appRieVictoria.models import Articulos,Clientes,compraProd,Compras,Empleados,ventaProd,Ventas,Proveedores,TipoPrenda,tipoFactura

class detalleVenta(admin.TabularInline):
    model = ventaProd

class ventaAdmin(admin.ModelAdmin):
    list_display= ("idEmpleado", "idClientes", "fecha", "tipoFactura")
    inlines = [detalleVenta]



class detalleCompra(admin.TabularInline):
    model = compraProd

class compraAdmin(admin.ModelAdmin):
    list_display= ("idEmpleado", "idProveedor", "fecha")
    inlines = [detalleCompra]

admin.site.register(Articulos)
admin.site.register(Clientes)
admin.site.register(compraProd)
admin.site.register(Compras, compraAdmin)
admin.site.register(Empleados)
admin.site.register(ventaProd)
admin.site.register(Ventas,ventaAdmin)
admin.site.register(Proveedores)
admin.site.register(TipoPrenda)
admin.site.register(tipoFactura)


admin.site.site_header = 'Rie Victoria'
admin.site.site_title = 'Rie Victoria'
admin.site.index_title = 'Rie Victoria'

