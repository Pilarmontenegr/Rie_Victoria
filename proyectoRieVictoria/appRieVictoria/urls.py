from django.urls import path
from .import views

urlpatterns = [path ('',views.index, name='index'),
               path ('index/',views.index, name='index'),
               path ('contador/',views.contador, name='contador'),
               path ('tabla/',views.tabla, name='tabla'),
               path ('articulos/<int:pk>/',views.articulos, name='articulos'),
               path ('clientes/',views.clientes, name='clientes'),
               path ('empleados/',views.empleados, name='empleados'),
               path ('proveedores/',views.proveedores, name='proveedores'),
               ]