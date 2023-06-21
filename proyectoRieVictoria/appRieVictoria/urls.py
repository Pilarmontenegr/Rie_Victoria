from django.urls import path
from .import views

urlpatterns = [path ('',views.index, name='index'),
               path ('contador/',views.contador, name='contador'),
               path ('bienvenida/',views.bienvenida, name='bienvenida'),
               path ('tabla/',views.tabla, name='tabla')
               ]