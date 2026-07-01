from abc import ABC, abstractmethod
#clase abstracta animal
#Principio: abstracción y encapsulamiento
print("El programa arrancó")
input("Presione enter")
class Animal(ABC):
    """
    Clase base abstracta que representa un animal.
    """
    def __init__(self, nombre, especie, edad):
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad
    #Getter nombre
    def get_nombre(self):
        return self.__nombre
    #Getter especie
    def get_especie(self):
        return self.__especie
    #Getter edad
    def get_edad(self):
        return self.__edad
    #Setter nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
    #Setter especie
    def set_especie(self, especie):
        self.__especie = especie
    #Setter edad
    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            raise ValueError("La edad no puede ser negativa")
    #Método abstracto
    @abstractmethod
    def calcular_costo_consulta(self):
        pass
    def __str__(self):
        return f"{self.__nombre} - {self.__especie} - {self.__edad} años"
#Clase perro
#Principio: herencia y polimorfismo
class Perro(Animal):
    """
    Representa un perro.
    """
    def __init__(self, nombre, especie, edad):
        super().__init__(nombre, especie, edad)
    #calcula el costo de la consulta
    def calcular_costo_consulta(self):
        return 5000
#clase gato
class Gato(Animal):
    """
    Representa un gato.
    """
    def __init__(self, nombre, especie, edad):
        super().__init__(nombre, especie, edad)
    #calcular el costo de la consulta
    def calcular_costo_consulta(self):
        return 4500
#clase  ave
class Ave(Animal):
    """
    Representa un ave.
    """
    def __init__(self, nombre, especie, edad):
        super().__init__(nombre, especie, edad)
    #calcular el costo de la consulta
    def calcular_costo_consulta(self):
        return 3500
#Clase Consulta
#Principio: Composición
class Consulta:
    """
    Representa una consulta veterinaria.
    """
    def __init__(self, animal, motivo, fecha):
        self.__animal = animal
        self.__motivo = motivo
        self.__fecha = fecha
    #mostrar detalles
    def mostrar_detalles(self):
        print("-----------------------")
        print(self.__animal)
        print("Motivo:", self.__motivo)
        print("Fecha:", self.__fecha)
        print("Costo:", self.__animal.calcular_costo_consulta())
    def get_costo(self):
        return self.__animal.calcular_costo_consulta()
    