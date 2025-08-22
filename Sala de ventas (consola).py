class Identificadores():
    def __init__(self,IdProductos,IdInventario,IdEmpleado,IdCliente,IdProveedor):
        self.IdProductos = IdProductos
        self.IdInventario = IdInventario
        self.IdEmpleado = IdEmpleado
        self.IdCliente = IdCliente
        self.IdProveedor = IdProveedor

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
    pass
class Inventario():
    pass
class Empleado():
    pass
class Cliente():
    pass
class Proveedor():
    pass
