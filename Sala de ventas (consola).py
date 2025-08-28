class Categoria():
    def __init__(self,IdCategoria,nombre):
        self.IdCategoria = IdCategoria
        self.nombre = nombre


    def AgregarCategoria(self, IdCategoria, nombre):
        self.categoria[IdCategoria] = {
            "nombre": nombre
        }


class producto():
    def __init__(self):
        self.productos = {}

    def AgregarProductos(self, IdProducto, nombre, precio_costo=0, precio_venta=0, stock=0):
        self.productos[IdProducto] = {
            "nombre": nombre,
            "precio_costo": precio_costo,
            "precio_venta": precio_venta,
            "stock": stock
        }


class Clientes():
    def __init__(self):
        self.clientes = {}
        self.CargarClientes()

    def CargarClientes(self):
        try:
            with open("Clientes.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea=linea.strip()
                    if linea:
                        nit,nombre,direccion,telefono,correo = linea.split(":")
                        self.clientes[nit] = {
                            "nombre" : nombre,
                            "direccion" : direccion,
                            "telefono" : telefono,
                            "correo" : correo
                        }
            print("Clientes importados desde clientes.txt")
        except FileNotFoundError:
            print("No existe el archivo Clientes.txt,se creara uno nuevo al guardar.")


    def GuardarClientes(self):
        with open("clientes.txt", "w", encoding="utf-8") as archivo:
            for nit,datos in self.clientes.items():
                archivo.write(f"{nit};{datos['nombre']}:{datos['direccion']}:{datos['telefono']}:{datos['correo']}\n")


    def AgregarCliente(self, nit, nombre, direccion, telefono, correo):
        self.clientes[nit] = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo
        }
        self.GuardarClientes()
        print(f"Cliente con NIT {nit} agregado correctamente.")

    def MostrarTodos(self):
        if self.clientes:
            print("\nLista de clientes: ")
            for nit,datos in self.clientes.items():
                print(f"\nNit : {nit}")
                for clave,valor in datos.items():
                    print(f"{clave} : {valor}")
        else:
            print("No hay clientes registrados.")

clientes =  Clientes()


class Proveedor():
    def __init__(self):
        self.proveedor = {}

    def AgregarProveedor(self, nit, nombre, direccion, telefono, correo, empresa):
        self.proveedor[nit] = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo,
            "empresa": empresa
        }


class Empleado():
    def __init__(self):
        self.empleado = {}

    def AgregarEmpleado(self, IdEmpleado, nombre, direccion, telefono, correo, puesto):
        self.empleado[IdEmpleado] = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo,
            "puesto": puesto
        }


'''---------------------------------------------------'''
'''AgregarIdEmpleado,NitClientes'''


class Ventas():
    def __init__(self):
        self.ventas = {}

    def AgregarVentas(self, IdVenta, fecha, total):
        self.ventas[IdVenta] = {
            "fecha": fecha,
            "total": total,
        }


'''--------------------------------------------------'''

'''__________________________________________________'''
'''AGREGAR IdVenta,IdProducto'''


class DetalleVenta():
    def __init__(self):
        self.detalleventas = {}

    def AgregarDetalleVenta(self, IdDetalleVenta, cantidad, subtotal, stock):
        self.detalleventas[IdDetalleVenta] = {
            "cantidad": cantidad,
            "subtotal": subtotal,
            "stock": stock
        }


'''_____________________________________________________________'''

'''**************************************************'''
'''AGREGAR IdEmpleado NitProveedores'''


class Compras():
    def __init__(self):
        self.compras = {}

    def AgregarCompras(self, IdCompra, fechaingreso, total):
        self.compras[IdCompra] = {
            "fechaingreso": fechaingreso,
            "total": total
        }


'''*******************************************************'''

'''/////////////////////////////////////////////////'''
'''AGREGAR IdVenta,IdProducto'''


class DetalleCompra():
    def __init__(self):
        self.detallecompra = {}

    def AgregarDetalleCompra(self, IdDetalleCompra, cantidad, subtotal, fechacaducidad):
        self.detallecompra[IdDetalleCompra] = {
            "cantidad": cantidad,
            "subtotal": subtotal,
            "fechacaducidad": fechacaducidad
        }


'''////////////////////////////////////////////////////////////////////////'''

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
    print("10. --Salir--")

    opcion = input("Escoja una opcion: ")

    if opcion == "3":
        print("Por favor ingrese los siguientes datos solicitados")
        nit = input("NIT: ")
        nombre = input("Nombre: ")
        direccion = input("Direccion: ")
        telefono = input("Telefono: ")
        correo = input("Correo: ")
        clientes.AgregarCliente(nit,nombre,direccion,telefono,correo)
    elif opcion == "2":
        clientes.MostrarTodos()