from django.urls import path
from .import views

urlpatterns = [path ('',views.index, name='index'),
               path ('index/',views.index, name='index'),
               path ('contador/',views.contador, name='contador'),
            
               path ('tablaCompras/',views.tablaCompras, name='tablaCompras'),
               path ('compras/<int:pk>/',views.compras, name='compras'),


               path('tablaVentas/', views.TablaVentas.as_view(), name='Ventas'),
               path('ventas/VentasNuevo/', views.VentasNuevo.as_view(), name='ventasNuevo'),
               path('ventas/VentasModif/<str:pk>/', views.VentasModif.as_view(), name='ventasModif'),
               path('ventas/VentasBorrar/<str:pk>/', views.VentasBorrar.as_view(), name='ventasBorrar'),  
               # path ('tablaVentas/',views.tablaVentas, name='tablaVentas'),
               # path ('ventas/<int:pk>/',views.ventas, name='ventas'),
              
               path ('tablaproveedores/',views.tablaproveedores, name='tablaproveedores'),
               path ('proveedores/<int:pk>/',views.proveedores, name='proveedores'),
               path('proveedores/ProveedoresNuevo/', views.ProveedoresNuevo, name='ProveedoresNuevo'),
               path('proveedores/ProveedoresModif/<str:pk>/', views.ProveedoresModif, name='ProveedoresModif'),
               path('proveedores/ProveedoresBorrar/<str:pk>/', views.ProveedoresBorrar, name='ProveedoresBorrar'),
               
               path ('tablaempleados/',views.tablaempleados, name='tablaempleados'),
               path ('empleados/<int:pk>/',views.empleados, name='empleados'),
               path('empleados/EmpleadosNuevo/', views.EmpleadosNuevo, name='EmpleadosNuevo'),
               path('empleados/EmpleadosModif/<str:pk>/', views.EmpleadosModif, name='EmpleadosModif'),
               path('empleados/EmpleadosBorrar/<str:pk>/', views.EmpleadosBorrar, name='EmpleadosBorrar'),
               
               
               path('tablaclientes/', views.TablaClientes.as_view(), name='clientes'),
               path('clientes/ClientesNuevo/', views.ClientesNuevo.as_view(), name='clientesNuevo'),
               path('clientes/ClientesModif/<str:pk>/', views.ClientesModif.as_view(), name='clientesModif'),
               path('clientes/ClientesBorrar/<str:pk>/', views.ClientesBorrar.as_view(), name='clientesBorrar'),  
               
               #path ('clientes/<int:pk>/',views.clientes, name='clientes'),


            #    path ('tablaclientes/',views.tablaclientes, name='tablaclientes'),
            
            #    path('clientes/ClientesNuevo/', views.ClientesNuevo, name='ClientesNuevo'),
            #    path('clientes/ClientesModif/<str:pk>/', views.ClientesModif, name='ClientesModif'),
            #    path('clientes/ClientesBorrar/<str:pk>/', views.ClientesBorrar, name='ClientesBorrar'),

               path('tabla/', views.tabla, name='tabla'),
               path ('articulos/<int:pk>/',views.Articulos, name='articulos'),
               path('articulo/ArticulosNuevo/', views.ArticulosNuevo, name='ArticulosNuevo'),
               path('articulos/ArticulosModif/<str:pk>/', views.ArticulosModif, name='ArticulosModif'),
               path('articulos/ArticulosBorrar/<str:pk>/', views.ArticulosBorrar, name='ArticulosBorrar'),

               ]

