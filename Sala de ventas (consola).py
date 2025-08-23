class Identificadores():
    def __init__(self,IdProductos,IdCategoria,IdCliente,IdProveedor,IdEmpleado,IdVentas,IdDetalleVenta,IdCompra,IdDetalleCompra):
        self.IdProductos = IdProductos
        self.IdCategoria = IdCategoria
        self.IdCliente = IdCliente
        self.IdProveedor = IdProveedor
        self.IdEmpleado = IdEmpleado
        self.IdVentas = IdVentas
        self.IdDetalleVenta = IdDetalleVenta
        self.IdCompra = IdCompra
        self.IdDetalleCompra = IdDetalleCompra

    def __str__(self):
        return (f"[{self.IdProductos} {self.IdCategoria} {self.IdCliente} "
                f"{self.IdProveedor} {self.IdEmpleado} {self.IdVentas} "
                f"{self.IdDetalleVenta} {self.IdCompra} {self.IdDetalleCompra}]")


class producto():
    def __init__(self):
        self.productos = {}


    def AgregarProductos(self,IdProducto,nombre,precio_costo,precio_venta,stock):
        self.productos[IdProducto] = {
            "nombre" : nombre,
            "precio_costo" : precio_costo,
            "precio_venta" : precio_venta,
            "stock" : stock
            }

class Categoria():
    '''IdCategoria,Nombre'''
    pass
class Cliente():
    '''NitCliente,Nombre,Direccion,Telefono,Correo'''
    pass
class Proveedor():
    '''NitProveedor,Nombre,Direccion,Telefono,Correo,Empresa'''
    pass
class Empleado():
    '''IdEmpleado,Nombre,Direccion,Telefono,Correo,Puesto'''
    pass
class Ventas():
    '''IdVenta,Fecha,IdEmpleado,IdCliente,Total'''
    pass
class DetalleVenta():
    '''IdDetalleVentas,IdVenta,CantidadmIdProducto,Subtotal,Stock'''
    pass
class Compras():
    '''IdCompra,FechaIngreso,IdEmpleado,IdProveedor,Total'''
    pass
class DetalleCompra():
    '''IDDetalleCompra,IdVenta,Cantidad,IdProducto,Subtotal,FechaCaducidad'''
    pass



