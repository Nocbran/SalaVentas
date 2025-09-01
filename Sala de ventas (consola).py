from sys import exec_prefix
from types import NotImplementedType

'''class AjustesVenta():
    def __init__(self):
        self.AjusteVenta = {}
        self.Eliminar()
        self.Actualizar()
        
    def Eliminar(self):
        while True: '''


class Categoria():
    def __init__(self):
        self.Categoria = {}
        self.CargarCategoria()
    def CargarCategoria(self):
        try:
            with open("Categorias.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea :
                        IdCategoria,nombre = linea.split(":")
                        self.Categoria[IdCategoria] = {
                            "nombre" : nombre
                        }
            print("Categorias importados desde Categorias.txt")
        except FileNotFoundError:
            print("No existe el archivo Categorias.txt, Se creara uno nuevo")

    def GuardarCategorias(self):
        with open("Categorias.txt","w", encoding="utf-8") as archivo:
            for IdCategoria, datos in self.Categoria.items():
                archivo.write(f"{IdCategoria}:{datos['nombre']}\n")


    def AgregarCategoria(self, IdCategoria, nombre):
        self.Categoria[IdCategoria] = {
            "nombre": nombre
        }
        self.GuardarCategorias()
        print(f"Categoria con ID {IdCategoria} agregado correctamente. ")

    def MostrarCategorias(self):
        if self.Categoria:
            print("\nLISTA DE CATEGORIAS: ")
            for IdCategoria,datos in self.Categoria.items():
                print(f"\nId Categoria: {IdCategoria}")
                for clave,valor in datos.items():
                    print(f"{clave} : {valor}")

categoria = Categoria()

class producto():
    def __init__(self):
        self.Productos = {}
        self.CargarProductos ()
    def CargarProductos(self):
        try:
            with open("Productos.txt","r",encoding="utf-8") as archivo:
                for liena in archivo:
                    linea = liena.strip()
                    if linea :
                        IdProducto,nombre,precio_costo,precio_venta,stock = linea.split(":")
                        self.Productos[IdProducto] = {
                            "nombre" : nombre,
                            "precio_costo": precio_costo,
                            "precio_venta": precio_venta,
                            "stock": stock
                        }
            print("Productos importados desde Productos.txt")
        except FileNotFoundError:
            print("No existe el archivo Productos, se creara uno nuevo")

    def GuardarProductos(self):
        with open("Productos.txt","w", encoding="utf-8") as archivo:
            for IdProducto, datos in self.Productos.items():
                archivo.write(f"{IdProducto}:{datos['nombre']}:{datos['precio_costo']}:{datos['precio_venta']}:{datos['stock']}\n")


    def AgregarProductos(self, IdProducto, nombre, precio_costo=0, precio_venta=0, stock=0):
        self.Productos[IdProducto] = {
            "nombre": nombre,
            "precio_costo": precio_costo,
            "precio_venta": precio_venta,
            "stock": stock
        }
        self.GuardarProductos()
        print(f"Producto con el ID {IdProducto} agregado correctamente")

Producto = producto()

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
                        NitClientes,nombre,direccion,telefono,correo = linea.split(":")
                        self.clientes[NitClientes] = {
                            "nombre" : nombre,
                            "direccion" : direccion,
                            "telefono" : telefono,
                            "correo" : correo
                        }
            print("Clientes importados desde clientes.txt")
        except FileNotFoundError:
            print("No existe el archivo Clientes.txt,se creara uno nuevo al guardar.")


    def GuardarClientes(self):
        with open("Clientes.txt", "w", encoding="utf-8") as archivo:
            for NitClientes,datos in self.clientes.items():
                archivo.write(f"{NitClientes}:{datos['nombre']}:{datos['direccion']}:{datos['telefono']}:{datos['correo']}\n")


    def AgregarCliente(self,NitClientes, nombre, direccion, telefono, correo):
        if NitClientes in self.clientes:
            print("El cliente ya existe!")
            return
        self.clientes[NitClientes] = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo
        }
        self.GuardarClientes()
        print(f"Cliente con NIT {NitClientes} agregado correctamente.")

    def MostrarClientes(self):
        if self.clientes:
            print("\nLista de clientes: ")
            for NitClientes,datos in self.clientes.items():
                print(f"\nNit : {NitClientes}")
                for clave,valor in datos.items():
                    print(f"{clave} : {valor}")
        else:
            print("No hay clientes registrados.")

clientes = Clientes()

class Proveedor():
    def __init__(self):
        self.proveedor = {}
        self.CargarProveedores()
    def CargarProveedores(self):
        try:
            with open("Proveedores.txt","r",encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea :
                        NitProveedor,nombre,direccion,telefono,correo,empresa = linea.split(":")
                        self.proveedor[NitProveedor] = {
                            "nombre": nombre,
                            "direccion": direccion,
                            "telefono": telefono,
                            "correo": correo,
                            "empresa": empresa
                        }
            print("Proveedores importado desde Proveedores.txt")
        except FileNotFoundError:
            print("No existe el archivo Proveedores, se creara uno nuevo.")


    def GuardarProveedor(self):
        with open("Proveedores.txt","w",encoding="utf-8") as archivo:
            for NitProveedor, datos in self.proveedor.items():
                archivo.write(f"{NitProveedor}:{datos['nombre']}:{datos['direccion']}:{datos['telefono']}:{datos['correo']}:{datos['empresa']}\n")


    def AgregarProveedor(self, NitProveedor, nombre, direccion, telefono, correo, empresa):
        self.proveedor[NitProveedor] = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo,
            "empresa": empresa
        }
        self.GuardarProveedor()
        print(f"Proveedor con el Nit {NitProveedor} agregado correctamente.")

proveedor = Proveedor()

class Empleado():
    def __init__(self):
        self.empleados = {}
        self.CargarEmpleado()
    def CargarEmpleado(self):
        try:
            with open("Empleados.txt", "r" , encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea :
                        NitEmpleado,nombre,direccion,telefono,correo,puesto = linea.split(":")
                        self.empleados[NitEmpleado] = {
                            "nombre": nombre,
                            "direccion": direccion,
                            "telefono": telefono,
                            "correo": correo,
                            "puesto": puesto
                        }
            print("Empleados importados desde Empleados.txt")
        except FileNotFoundError:
            print("No existe el archivo Empleados.txt, se creara uno nuevo.")

    def GuardarEmpleados(self):
        with open("Empleados.txt", "w" , encoding="utf-8") as archivo:
            for NitEmpleado,datos in self.empleados.items():
                archivo.write(f"{NitEmpleado}:{datos['nombre']}:{datos['direccion']}:{datos['telefono']}:{datos['correo']}:{datos['puesto']}\n")

    def AgregarEmpleado(self, NitEmpleado, nombre, direccion, telefono, correo, puesto):
        self.empleados[NitEmpleado] = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo,
            "puesto": puesto
        }
        self.GuardarEmpleados()
        print(f"Empleado con el NIT {NitEmpleado} agregado correctamente.")
empleado = Empleado()
'''---------------------------------------------------'''
'''AgregarIdEmpleado,NitClientes'''

class Ventas():
    def __init__(self):
        self.ventas = {}
        self.CargarVentas()
    def CargarVentas(self):
        try:
            with open("Ventas.txt","r",encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea :
                        Idventa,fecha,NitClientes,NitEmpleado,total = linea.split(":")
                        self.ventas[Idventa] = {
                            "fecha": fecha,
                            "nit_cliente": NitClientes,
                            "nit_empleado": NitEmpleado,
                            "total": total
                        }
            print("Ventas importados desde Ventas.txt")
        except FileNotFoundError:
            print("No existe el archivo Ventas.txt, se creara uno nuevo")

    def GuardarVentas(self):
        with open("Ventas.txt","w",encoding="utf-8") as archivo:
            for IdVenta,datos in self.ventas.items():
                archivo.write(f"{IdVenta}:{datos['fecha']}:{datos['nit_cliente']}:{datos['nit_empleado']}:{datos['total']}\n")

    def AgregarVentas(self, IdVenta, fecha, NitClientes, NitEmpleado, total):
        if NitClientes not in clientes.clientes:
            print(f" El cliente con NIT {NitClientes} no existe.")
            return

        if NitEmpleado not in empleado.empleados:
            print(f"El empleado con NIT {NitEmpleado} no existe.")
            return

        self.ventas[IdVenta] = {
            "fecha": fecha,
            "nit_cliente": NitClientes,
            "nit_empleado": NitEmpleado,
            "total": total
        }
        self.GuardarVentas()
        print(f"✅ Venta con el ID {IdVenta}, guardada correctamente.")
ventas = Ventas()
'''--------------------------------------------------'''

class DetalleVenta():
    def __init__(self):
        self.Detalleventas = {}
        self.CargarDetalleVenta()
    def CargarDetalleVenta(self):
        try:
            with open("Detalleventas.txt","r",encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea :
                        IdDetalleVenta, IdVenta, IdProducto, cantidad, subtotal = linea.split(":")
                        self.Detalleventas[IdDetalleVenta] = {
                            "IdVenta": IdVenta,
                            "IdProducto": IdProducto,
                            "cantidad": int(cantidad),
                            "subtotal": float(subtotal)
                        }
                    print("Detalleventas.txt importados desde Detalleventas")
        except FileNotFoundError:
            print("No existe el archivo Detalleventas.txt. se creara uno nuevo.")

    def GuardarDetalleVenta(self):
        with open("Detalleventas.txt", "w", encoding="utf-8") as archivo:
            for IdDetalleVenta, datos in self.Detalleventas.items():
                archivo.write(
                    f"{IdDetalleVenta}:{datos['IdVenta']}:{datos['IdProducto']}:{datos['cantidad']}:{datos['subtotal']}\n")

    def AgregarDetalleVenta(self, IdDetalleVenta, IdVenta, IdProducto, cantidad):
                # Verificar que la venta exista
        if IdVenta not in ventas.ventas:
            print(f"La venta {IdVenta} no existe.")
            return
                # Verificar que el producto exista
        if IdProducto not in Producto.Productos:
            print(f"El producto {IdProducto} no existe.")
            return
                # Verificar stock
        stock_disponible = int(Producto.Productos[IdProducto]["stock"])
        if cantidad > stock_disponible:
            print(f"No hay suficiente stock. Disponible: {stock_disponible}")
            return

                # Calcular subtotal
        precio_venta = float(Producto.Productos[IdProducto]["precio_venta"])
        subtotal = cantidad * precio_venta

                # Restar stock
        Producto.Productos[IdProducto]["stock"] = str(stock_disponible - cantidad)
        Producto.GuardarProductos()

                # Guardar detalle
        self.Detalleventas[IdDetalleVenta] = {
            "IdVenta": IdVenta,
            "IdProducto": IdProducto,
            "cantidad": cantidad,
            "subtotal": subtotal
            }
        self.GuardarDetalleVenta()
        print(f"✅ Detalle de venta agregado correctamente (Producto {IdProducto}, Cantidad {cantidad})")
detalleventa = DetalleVenta()
'''_____________________________________________________________'''

'''**************************************************'''
'''AGREGAR IdEmpleado NitProveedores'''

class Compras():
    def __init__(self):
        self.Compras = {}
        self.CargarCompras()
    def CargarCompras(self):
        try:
            with open("Compras.txt","r",encoding="utf-8")as arvhivo:
                for linea in arvhivo:
                    linea=linea.strip()
                    if linea :
                        IdCompras,fechaingreso,total = linea.split(":")
                        self.Compras[IdCompras] = {
                            "fechaingreso": fechaingreso,
                            "total": total
                        }
            print("Compras importadas desde Compras.txt")
        except FileNotFoundError:
            print("No existe el arvhivo Compras.txt, se creara uno nuevo.")

    def GuardarCompras(self):
        with open("Compras.txt","w",encoding="utf-8")as archivo:
            for IdCompras,datos in self.Compras.items():
                archivo.write(f"{IdCompras}:{datos['fechaingreso']}:{datos['total']}\n")

    def AgregarCompras(self, IdCompra, fechaingreso, total):
        self.Compras[IdCompra] = {
            "fechaingreso": fechaingreso,
            "total": total
        }
        self.GuardarCompras()
        print("Compras guardadas correctamente.")
compras = Compras()
'''*******************************************************'''

'''/////////////////////////////////////////////////'''
'''AGREGAR IdVenta,IdProducto'''

class DetalleCompra():
    def __init__(self):
        self.DetalleCompra = {}
        self.CargarDetalleCompra()
    def CargarDetalleCompra(self):
        try:
            with open("DetalleCompra.txt","r",encoding="utf-8")as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea :
                        IdDetalleCompra,cantidad,subtotal,fechacaducidad = linea.split(":")
                        self.DetalleCompra[IdDetalleCompra] = {
                            "cantidad": cantidad,
                            "subtotal": subtotal,
                            "fechacaducidad": fechacaducidad
                        }
            print("Detalles de compra guardadas correctamente")
        except FileNotFoundError:
            print("No existe DetalleCompra.txt, se creara uno nuevo")

    def GuardarDetalleCompra(self):
        with open("DetalleCompra.txt","w",encoding="utf-8")as archivo:
            for IdDetalleCompra,datos in self.DetalleCompra.items():
                archivo.write(f"{IdDetalleCompra}:{datos['cantidad']}:{datos['subtotal']}:{datos['fechacaducidad']}\n")

    def AgregarDetalleCompra(self, IdDetalleCompra, cantidad, subtotal, fechacaducidad):
        self.DetalleCompra[IdDetalleCompra] = {
            "cantidad": cantidad,
            "subtotal": subtotal,
            "fechacaducidad": fechacaducidad
        }
        self.GuardarDetalleCompra()
        print(f"Detalles de compra con el ID {IdDetalleCompra},agregado correctamente.")

detallecompra = DetalleCompra()
'''////////////////////////////////////////////////////////////////////////'''

def menu():
    while True:
        print("\n *****BIENVENIDO A LA SALA DE VENTAS*****")
        print("1. --Ventas--")
        print("2. --Agregar producto--")
        print("3. --Agregar categoria--")
        print("4. --Agregar clientes--")
        print("5. --Mostrar cliente--")
        print("6. --Agregar proveedor--")
        print("7. --Agregar empleado--")
        print("8. --Salir--")

        opcion = input("Escoja una opcion: ")

        opciones = {
            "1": lambda : ventas.AgregarVentas(
                input("Igrese el Id de ventas: "),
                input("Ingrese la fecha: "),
                input("Ingrese el ID del empleado: "),
                input("Ingrese el Nit del cliente: "),
                input("Ingrese el total: "),
            ),


            "2": lambda: Producto.AgregarProductos(
                input("ID Producto: "),
                input("Nombre: "),
                input("Precio costo: "),
                input("Precio_venta: "),
                input("stock: "),
            ),
            "3": lambda: categoria.AgregarCategoria(
                input("ID Categoria: "),
                input("Nombre: "),
            ),
            "4": lambda : clientes.AgregarCliente(
                input("Nit: "),
                input("Nombre: "),
                input("Direccion: "),
                input("Telefono: "),
                input("Correo: "),
            ),
            "5": lambda : clientes.MostrarClientes(),
            "6" : lambda : proveedor.AgregarProveedor(
                input("Nit Proveedor: "),
                input("Nombre: "),
                input("Direccion: "),
                input("Telefono: "),
                input("Correo: "),
                input("Empresa: ")
            ),
            "7": lambda : empleado.AgregarEmpleado(
                input("Nit Empleado: "),
                input("Nombre: "),
                input("Direccion: "),
                input("Telefono: "),
                input("Correo: "),
                input("Puesto: "),
            ),
            "8": lambda : exit()

        }
        if opcion in opciones:
            opciones[opcion]()
        else:
            print("Opcion invalida, intentelo de nuevo.")

menu()