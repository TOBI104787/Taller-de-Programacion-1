#Clase base
class Producto:
    def __init__(self, codigo, nombre, stock, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__stock = stock
        self.__precio = precio
    #GETTERS
    def get_codigo(self):
        return self.__codigo
    def get_nombre(self):
        return self.__nombre
    def get_stock(self):
        return self.__stock
    def get_precio(self):
        return self.__precio
    #SETTERS
    def set_stock(self, nuevo_stock):
        if nuevo_stock >= 0:
            self.__stock = nuevo_stock
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
    #Método polimórfico
    def mostrar_info(self):
        print("Código:", self.__codigo)
        print("Nombre:", self.__nombre)
        print("Stock:", self.__stock)
        print("Precio:", self.__precio)
#Clase derivada
class ProductoPerecedero(Producto):
    def __init__(self, codigo, nombre, stock, precio, fecha_vencimiento):
        #Uso de super()
        super().__init__(codigo, nombre, stock, precio)
        self.__fecha_vencimiento = fecha_vencimiento
    #Getter
    def get_fecha_vencimiento(self):
        return self.__fecha_vencimiento
    #Setter
    def set_fecha_vencimiento(self, nueva_fecha):
        self.__fecha_vencimiento = nueva_fecha
    #Polimorfismo
    def mostrar_info(self):
        super().mostrar_info()
        print("Fecha de vencimiento:", self.__fecha_vencimiento)
#Lista de productos
productos = []
#Función agregar producto
def agregar_producto():
    if len(productos) >= 10:
        print("No se pueden agregar más de 10 productos")
        return
    codigo = input("Ingrese código: ")
    # Validar código repetido
    for producto in productos:
        if producto.get_codigo() == codigo:
            print("El código ya existe")
            return
    nombre = input("Ingrese nombre: ")
    stock = int(input("Ingrese stock: "))
    precio = float(input("Ingrese precio: "))
    tipo = input("¿Es perecedero? (si/no): ")
    if tipo.lower() == "si":
        fecha = input("Ingrese fecha de vencimiento: ")
        producto = ProductoPerecedero(
            codigo,
            nombre,
            stock,
            precio,
            fecha
        )
    else:
        producto = Producto(
            codigo,
            nombre,
            stock,
            precio
        )
    productos.append(producto)
    print("Producto agregado correctamente")
#Buscar producto
def buscar_producto():
    codigo = input("Ingrese código a buscar: ")
    encontrado = False
    for producto in productos:
        if producto.get_codigo() == codigo:
            print("\nProducto encontrado")
            producto.mostrar_info()
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado")
# Listar productos
def listar_productos():
    if len(productos) == 0:
        print("No hay productos cargados")
    else:
        for producto in productos:

            print("\n----------------")
            producto.mostrar_info()
#Total stock
def total_stock():
    total = 0
    for producto in productos:
        total += producto.get_stock()
    print("Total de stock:", total)
#Menú principal
while True:
    print("\n===== SISTEMA DE STOCK =====")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Listar productos")
    print("4. Consultar stock total")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        buscar_producto()
    elif opcion == "3":
        listar_productos()
    elif opcion == "4":
        total_stock()
    elif opcion == "5":
        print("Programa finalizado")
        break
    else:
        print("Opción inválida")