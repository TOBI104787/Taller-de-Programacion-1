class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
class Zapato(Producto):
    def descripcion(self):
        print("Zapato: (self.nombre), (self.precio)")

class Sandalia(Producto):
    def descripcion(self):
        return f"Sandalia: {self.nombre} - ${self.precio}"
class metodo_de_pago:
    def pagar(self, monto):
        pass
class Tarjeta(metodo_de_pago):
    def pagar(self, monto):
        return f"Pagando ${monto} con tarjeta."

class PayPal(metodo_de_pago):
    def pagar(self, monto):
        return f"Pagando ${monto} con PayPal."
class Pedido:
    def __init__(self, producto):
        self.producto = producto
        self.pagado = False

    def verificar_disponibilidad(self):
        # Simulación
        return True

    def procesar_pago(self, metodo_pago: metodo_de_pago):
        if self.verificar_disponibilidad():
            print(metodo_pago.pagar(self.producto.precio))
            self.pagado = True
        else:
            print("Producto no disponible.")

    def confirmar(self):
        if self.pagado:
            return "Pedido confirmado. Factura generada."
        return "Pago pendiente."

    def enviar(self):
        if self.pagado:
            return "Producto enviado al cliente."
        return "No se puede enviar sin pago."