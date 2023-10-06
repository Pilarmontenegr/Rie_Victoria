from django.urls import path
from .import views

urlpatterns = [path ('',views.index, name='index'),
               path ('index/',views.index, name='index'),
               path ('contador/',views.contador, name='contador'),
            
            #    path ('tablaCompras/',views.tablaCompras, name='tablaCompras'),
            #    path ('compras/<int:pk>/',views.compras, name='compras'),
               path('tablaCompras/', views.TablaCompras.as_view(), name='Compras'),
               path('compras/ComprasNuevo/', views.ComprasNuevo.as_view(), name='ComprasNuevo'),
               path('compras/ComprasModif/<int:pk>/', views.ComprasModif.as_view(), name='ComprasModif'),
               path('compras/ComprasBorrar/<int:pk>/', views.ComprasBorrar.as_view(), name='ComprasBorrar'),  


               path('tablaVentas/', views.TablaVentas.as_view(), name='Ventas'),
               path('ventas/VentasNuevo/', views.VentasNuevo.as_view(), name='ventasNuevo'),
               path('ventas/VentasModif/<int:pk>/', views.VentasModif.as_view(), name='ventasModif'),
               path('ventas/VentasBorrar/<int:pk>/', views.VentasBorrar.as_view(), name='ventasBorrar'),  
               # path ('tablaVentas/',views.tablaVentas, name='tablaVentas'),
               # path ('ventas/<int:pk>/',views.ventas, name='ventas'),
              
               path ('tablaproveedores/',views.tablaproveedores, name='tablaproveedores'),
               path ('proveedores/<int:pk>/',views.proveedores, name='proveedores'),
               path('proveedores/ProveedoresNuevo/', views.ProveedoresNuevo, name='ProveedoresNuevo'),
               path('proveedores/ProveedoresModif/<int:pk>/', views.ProveedoresModif, name='ProveedoresModif'),
               path('proveedores/ProveedoresBorrar/<int:pk>/', views.ProveedoresBorrar, name='ProveedoresBorrar'),
               
               path ('tablaempleados/',views.tablaempleados, name='tablaempleados'),
               path ('empleados/<int:pk>/',views.empleados, name='empleados'),
               path('empleados/EmpleadosNuevo/', views.EmpleadosNuevo, name='EmpleadosNuevo'),
               path('empleados/EmpleadosModif/<int:pk>/', views.EmpleadosModif, name='EmpleadosModif'),
               path('empleados/EmpleadosBorrar/<int:pk>/', views.EmpleadosBorrar, name='EmpleadosBorrar'),
               
               
               path ('clientes/<int:pk>/',views.clientes, name='clientes'),
               path ('tablaclientes/',views.tablaclientes, name='tablaclientes'),
               path('clientes/ClientesNuevo/', views.ClientesNuevo, name='ClientesNuevo'),
               path('clientes/ClientesModif/<int:pk>/', views.ClientesModif, name='ClientesModif'),
               path('clientes/ClientesBorrar/<int:pk>/', views.ClientesBorrar, name='ClientesBorrar'),

               path('tabla/', views.tabla, name='tabla'),
               path ('articulos/<int:pk>/',views.Articulos, name='articulos'),
               path('articulo/ArticulosNuevo/', views.ArticulosNuevo, name='ArticulosNuevo'),
               path('articulos/ArticulosModif/<int:pk>/', views.ArticulosModif, name='ArticulosModif'),
               path('articulos/ArticulosBorrar/<int:pk>/', views.ArticulosBorrar, name='ArticulosBorrar'),

               ]

