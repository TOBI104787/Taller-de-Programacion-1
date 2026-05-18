class Producto:
    def __init__(self, nombre, precio, cantidad_en_stock):
    #atributos privados
     self.__nombre = nombre
     self.__precio = precio
     self.__cantidad_en_stock = cantidad_en_stock
    #Métodos GET
    def get_nombre(self):
        return self.__nombre
    def get_precio(self):
        return self.__precio
    def get_stock(self):
        return self.__cantidad_en_stock
    #Métodos SET
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Precio inválido")
    #Manejo de stock
    def agregar_stock(self, cantidad):
        if cantidad > 0:
            self.__cantidad_en_stock += cantidad
        else:
            print("Cantidad inválida")
    def retirar_stock(self, cantidad):
        if 0 < cantidad <= self.__cantidad_en_stock:
            self.__cantidad_en_stock -= cantidad
        else:
            print("No hay suficiente stock o cantidad inválida")
producto1 = Producto("Laptop", 1500, 10)
print(producto1.get_nombre())
print(producto1.get_precio())
print(producto1.get_stock())
producto1.agregar_stock(5)
print("Stock después de agregar:", producto1.get_stock())
producto1.retirar_stock(8)
print("Stock después de retirar:", producto1.get_stock())
producto1.set_precio(1700)
print("Nuevo precio:", producto1.get_precio())