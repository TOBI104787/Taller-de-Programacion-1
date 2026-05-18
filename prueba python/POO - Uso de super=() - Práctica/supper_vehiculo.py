#Clase base:
class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
#Clase derivada:
class automovil(vehiculo):
    def __init__(self, marca, modelo, puertas):
        #Atributo propio de Automovil
        self.puertas = puertas
        #Usamos super() para llamar al constructor de Vehiculo
        super().__init__(marca, modelo)
    def mostrar(self):
        return f"auto: {self.marca} {self.modelo} {self.puertas}"
mi_auto = automovil("fiat", "cronos", "4 puertas")
print(mi_auto.mostrar())