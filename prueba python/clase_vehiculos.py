from abc import ABC, abstractmethod

class Vehiculo(ABC):
    
    @abstractmethod
    def mostrar_info(self):
        pass
class Auto(Vehiculo):
    def mostrar_info(self):
        return "Un auto: 4 ruedas, ideal para ciudad."

class Moto(Vehiculo):
    def mostrar_info(self):
        return "Una moto: rápida y ágil."

class Camion(Vehiculo):
    def mostrar_info(self):
        return "Un camión: transporte de carga pesada."
def main():
    # Crear objetos de diferentes tipos
    vehiculos = [Auto(), Moto(), Camion()]

    # Polimorfismo: misma llamada, diferente comportamiento
    for vehiculo in vehiculos:
        print(vehiculo.mostrar_info())


if __name__ == "__main__":
    main()