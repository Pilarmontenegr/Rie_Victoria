from django.urls import path
from .import views

urlpatterns = [path ('',views.index, name='index'),
               path ('index/',views.index, name='index'),
               path ('contador/',views.contador, name='contador'),
               path ('tabla/',views.tabla, name='tabla'),
               path ('articulos/<int:pk>/',views.articulos, name='articulos'),
               path ('tablaclientes/',views.tablaclientes, name='tablaclientes'),
               path ('clientes/<int:pk>/',views.clientes, name='clientes'),
               path ('tablaempleados/',views.tablaempleados, name='tablaempleados'),
               path ('empleados/<int:pk>/',views.empleados, name='empleados'),
               path ('proveedores/',views.proveedores, name='proveedores'),
               path ('tablaCompras/',views.tablaCompras, name='tablaCompras'),
               path ('compras/<int:pk>/',views.compras, name='compras'),
               path ('tablaVentas/',views.tablaVentas, name='tablaVentas'),
               ]