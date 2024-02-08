from django.db import models

class Proveedores(models.Model):
    nombre = models.CharField(max_length=25, help_text="Nombre del proveedor",verbose_name="Nombre")
    direccion = models.CharField(max_length=100, help_text="Direccion del proveedor",verbose_name="Dirección")
    Email = models.EmailField(help_text="Email del proveedor")
    cuit = models.PositiveBigIntegerField(help_text="Cuit del proveedor",verbose_name="Cuit")
    telefono = models.PositiveBigIntegerField()
    empleados = models.ManyToManyField("Empleados",related_name='empleados_compran_a_proveedores', through="Compras",verbose_name="Empleado")
    def __str__(self) -> str:
        return str(self.nombre)
    
    class Meta:
        permissions = [
            ("puede_aprobar", "Puede aprobar el modelo"),
            ("puede_publicar", "Puede publicar el modelo"),
        ]

class Empleados(models.Model):
    nombre = models.CharField(max_length=50, help_text="Nombre del empleado",verbose_name="Nombre")
    direccion = models.CharField(max_length=100, help_text='Direccion del empleado')
    Email = models.EmailField(help_text="Email del empleado")
    telefono = models.PositiveBigIntegerField(help_text='Telefono del empleado')
    proveedores = models.ManyToManyField("Proveedores" ,related_name='venden_a_empleados', through="Compras")
    clientes = models.ManyToManyField("Clientes" ,related_name='empleados_relacionados', through="Ventas")
    def __str__(self) -> str:
        return str(self.nombre)
    class Meta:
        permissions = [
            ("puede_aprobar", "Puede aprobar el modelo"),
            ("puede_publicar", "Puede publicar el modelo"),
        ]

class Compras(models.Model):
    idProveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    idEmpleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    fecha = models.DateField(help_text="Fecha de compra")
    #articulos = models.ManyToManyField("Articulos" ,related_name='articulos_comprados', through="CompraProd")
    def __str__(self) -> str:
        return str(self.idProveedor)

class Clientes (models.Model):
    nombre = models.CharField(max_length=100, help_text= 'Nombre del cliente')
    direccion = models.CharField(max_length=100, help_text='Direccion del proveedor')
    DNI = models.PositiveBigIntegerField(help_text='Dni del cliente')
    telefono = models.PositiveBigIntegerField(help_text='Telefono del cliente')
    empleados = models.ManyToManyField("Empleados" ,related_name='clientes_relacionados', through="Ventas")
    def __str__(self) -> str:
        return str(self.nombre)
        

class Ventas(models.Model):
    idEmpleado = models.ForeignKey(Empleados, on_delete=models.CASCADE,verbose_name="Empleado")
    idClientes = models.ForeignKey(Clientes, on_delete=models.CASCADE,verbose_name="Cliente")
    fecha = models.DateField(help_text="Fecha de venta",verbose_name="Fecha")
    articulos = models.ManyToManyField("Articulos" ,related_name='ventas_productos', through="ventaProd")
    tipoFactura =models.ForeignKey("tipoFactura", on_delete=models.CASCADE, default=1, verbose_name="Tipo de Factura")


class tipoFactura(models.Model):
    descripcion =models.CharField( max_length= 2,help_text= 'Tipo de factura')
    def __str__(self) -> str:
        return str(self.descripcion)

class Articulos (models.Model):
    descripcion = models.CharField( max_length= 100,help_text= 'Descripcion del articulo')
    
    venta= models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.BigIntegerField(help_text='Cantidad de articulos')
    talle = models.CharField(max_length=3)
    #compras = models.ManyToManyField("Compras",related_name='articulos_comprados' , through="CompraProd")
    ventas = models.ManyToManyField("Ventas" ,related_name='articulos_vendidos', through="ventaProd")
    tipoPrenda =models.ForeignKey("tipoPrenda", on_delete=models.CASCADE, default=1)
    
    def __str__(self) -> str:
        return str(self.id)+" | "+str(self.descripcion)

class TipoPrenda (models.Model):
    descripcion =models.CharField( max_length= 60,help_text= 'Tipo de articulo')
    def __str__(self) -> str:
        return str(self.descripcion)


class CompraProd(models.Model):
    idCompra = models.ForeignKey(Compras,on_delete=models.CASCADE)
    #idArticulos = models.ForeignKey(Articulos, on_delete=models.CASCADE)
    descripcionArticulo = models.CharField(max_length=30 ,help_text='Articulo comprado')
    cantidad = models.BigIntegerField(help_text='cantidad de articulos')
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    totalCompra = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return str(self.idCompra)


class VentaProd(models.Model):
    idVenta = models.ForeignKey(Ventas, on_delete= models.CASCADE)
    idArticulos = models.ForeignKey(Articulos,on_delete=models.CASCADE)
    cantidad = models.BigIntegerField(help_text='Cantidad de ventas')
    precioVenta = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    totalVenta = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self) -> str:
        return str(self.idVenta)