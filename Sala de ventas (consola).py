class Identificadores():
    def __init__(self,IdProductos,IdCategoria,,IdCliente,IdProveedor,IdEmpleado,IdVentas,IdDetalleVenta,IdCompra,IdDetalleCompra):
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
        return f"[{self.IdProductos} {self.IdInventario} {self.IdEmpleado} {self.IdCliente} {self.IdProveedor} ]"


class producto():
    def __init__(self,nombre,categoria,precio_costo,precio_venta,stock):
        self.nombre = nombre
        self.categoria = categoria
        self.precio_costo = precio_costo
        self.precio_venta = precio_venta
        self.stock = stock

    def __str__(self):
        return f"[{self.nombre} {self.categoria} {self.precio_costo} {self.precio_venta} {self.stock}]"

class Productos():
    '''nombre,precio,IdCategoria'''
    pass
class Categoria():
    pass
class Cliente():
    pass
class Proveedor():
    pass
class Empleado():
    pass
class Ventas():
    pass
class DetalleVenta():
    pass
class Compras():
    pass
class DetalleCompra():
    pass



