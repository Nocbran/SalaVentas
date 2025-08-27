'''class Identificadores():
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
                f"{self.IdDetalleVenta} {self.IdCompra} {self.IdDetalleCompra}]")'''
from faulthandler import cancel_dump_traceback_later


class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre


class Producto:
    def __init__(self, id_producto, nombre, id_categoria, stock=0, precio_costo=0,precio_venta =0):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio_costo = precio_costo
        self.precio_venta = precio_venta
        self.id_categoria = id_categoria
        self.stock = stock
        self.total_compras = 0
        self.total_ventas = 0


class Cliente:
    def __init__(self, nit, nombre, direccion, telefono,correo):
        self.nit = nit
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

class Empleado:
    def __init__(self, id_empleado, nombre, puesto):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.puesto = puesto


class Venta:
    def __init__(self, id_venta, fecha, nit_cliente, id_empleado):
        self.id_venta = id_venta
        self.fecha = fecha
        self.nit_cliente = nit_cliente
        self.id_empleado = id_empleado
        self.detalles = {}  # {id_producto: (cantidad, subtotal)}

    def agregar_detalle(self, producto, cantidad):
        if producto.stock >= cantidad:
            subtotal = producto.precio * cantidad
            self.detalles[producto.id_producto] = (cantidad, subtotal)
            producto.stock -= cantidad
            producto.total_ventas += cantidad
        else:
            print("Stock insuficiente")


class Compra:
    def __init__(self, id_compra, fecha, nit_proveedor, id_empleado):
        self.id_compra = id_compra
        self.fecha = fecha
        self.nit_proveedor = nit_proveedor
        self.id_empleado = id_empleado
        self.detalles = {}  # {id_producto: (cantidad, subtotal)}

    def agregar_detalle(self, producto, cantidad, precio_costo):
        subtotal = precio_costo * cantidad
        self.detalles[producto.id_producto] = (cantidad, subtotal)
        producto.stock += cantidad
        producto.total_compras += cantidad


productos = {}
categorias = {}
clientes = {}
empleados = {}
ventas = {}
compras = {}


while True:
    print("\n *****BIENVENIDO A LA SALA DE VENTAS*****")
    print("1. --Agregar producto--")
    print("2. --Agregar categoria--")
    print("3. --Agregar clientes--")
    print("4. --Agregar proveedores--")
    print("5. --Agregar empleados--")
    print("6. --Agregar ventas--")
    print("7. --Agregar detalles de ventas--")
    print("8. --Agregar compras--")
    print("9. --Agregar detalle de compras--")
    print("10. Salir")


