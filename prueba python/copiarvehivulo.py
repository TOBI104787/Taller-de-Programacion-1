# Clase base
class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)


# Clase derivada
class Automovil(Vehiculo):

    def __init__(self, marca, modelo, numero_de_puertas):
        # Usamos super() para llamar al constructor de Vehiculo
        super().__init__(marca, modelo)

        # Atributo propio de Automovil
        self.numero_de_puertas = numero_de_puertas

    def mostrar_info_completa(self):
        # Reutilizamos el método de la clase base
        super().mostrar_info()

        # Información adicional
        print("Número de puertas:", self.numero_de_puertas)
auto1 = Automovil("Toyota", "Corolla", 4)

auto1.mostrar_info_completa()