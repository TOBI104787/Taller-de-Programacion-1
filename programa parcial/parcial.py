from abc import ABC, abstractmethod
# Clase abstracta Animal
# Principio: Abstracción y Encapsulamiento
print("El programa arrancó")
input("Presioná Enter...")
class Animal(ABC):
    """
    Clase base abstracta que representa un animal.
    """
    def __init__(self, nombre, especie, edad):
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad
    # Getter nombre
    def get_nombre(self):
        return self.__nombre
    # Getter especie
    def get_especie(self):
        return self.__especie
    # Getter edad
    def get_edad(self):
        return self.__edad
    # Setter nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
    # Setter especie
    def set_especie(self, especie):
        self.__especie = especie
    # Setter edad
    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            raise ValueError("La edad no puede ser negativa")
    # Método abstracto
    @abstractmethod
    def calcular_costo_consulta(self):
        pass
    def __str__(self):
        return f"{self.__nombre} - {self.__especie} - {self.__edad} años"
# Clase Perro
# Principio: Herencia y Polimorfismo
class Perro(Animal):
    """
    Representa un perro.
    """
    def __init__(self, nombre, especie, edad):
        super().__init__(nombre, especie, edad)
    # Calcula costo de consulta
    def calcular_costo_consulta(self):
        return 5000
# Clase Gato
class Gato(Animal):
    """
    Representa un gato.
    """
    def __init__(self, nombre, especie, edad):
        super().__init__(nombre, especie, edad)
    # Calcula costo de consulta
    def calcular_costo_consulta(self):
        return 4500
# Clase Ave
class Ave(Animal):
    """
    Representa un ave.
    """
    def __init__(self, nombre, especie, edad):
        super().__init__(nombre, especie, edad)
    # Calcula costo de consulta
    def calcular_costo_consulta(self):
        return 3500
# Clase Consulta
# Principio: Composición
class Consulta:
    """
    Representa una consulta veterinaria.
    """
    def __init__(self, animal, motivo, fecha):
        self.__animal = animal
        self.__motivo = motivo
        self.__fecha = fecha
    # Mostrar detalle
    def mostrar_detalle(self):
        print("-----------------------")
        print(self.__animal)
        print("Motivo:", self.__motivo)
        print("Fecha:", self.__fecha)
        print("Costo:", self.__animal.calcular_costo_consulta())
    def get_costo(self):
        return self.__animal.calcular_costo_consulta()
# Clase Veterinaria
# Principio: Encapsulamiento
class Veterinaria:
    """
    Gestiona pacientes y consultas.
    """
    def __init__(self):
        self.__pacientes = []
        self.__consultas = []
    # Registrar paciente
    def registrar_paciente(self, animal):
        self.__pacientes.append(animal)
        print("Paciente registrado.")
    # Registrar consulta
    def registrar_consulta(self, consulta):
        self.__consultas.append(consulta)
        print("Consulta registrada.")
    # Mostrar historial
    def mostrar_historial(self):
        if len(self.__consultas) == 0:
            print("No hay consultas.")
        else:
            for consulta in self.__consultas:
                consulta.mostrar_detalle()
    # Calcular ingresos
    def calcular_ingresos_totales(self):
        total = 0
        for consulta in self.__consultas:
            total += consulta.get_costo()
        print("Ingresos totales: $", total)
    # Buscar paciente
    def buscar_paciente(self, nombre):
        for paciente in self.__pacientes:
            if paciente.get_nombre().lower() == nombre.lower():
                return paciente
        return None
# Programa principal
veterinaria = Veterinaria()
while True:
    print("\n===== CLÍNICA VETERINARIA =====")
    print("1. Registrar paciente")
    print("2. Registrar consulta")
    print("3. Mostrar historial")
    print("4. Calcular ingresos")
    print("5. Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        try:
            print("\n1. Perro")
            print("2. Gato")
            print("3. Ave")
            tipo = input("Tipo: ")
            nombre = input("Nombre: ")
            especie = input("Especie: ")
            edad = int(input("Edad: "))
            if edad < 0:
                raise ValueError("Edad inválida")
            if tipo == "1":
                animal = Perro(nombre, especie, edad)
            elif tipo == "2":
                animal = Gato(nombre, especie, edad)
            elif tipo == "3":
                animal = Ave(nombre, especie, edad)
            else:
                print("Tipo incorrecto")
                continue
            veterinaria.registrar_paciente(animal)
        except ValueError as error:
            print(error)
    elif opcion == "2":
        nombre = input("Nombre del paciente: ")
        paciente = veterinaria.buscar_paciente(nombre)
        if paciente:
            motivo = input("Motivo: ")
            fecha = input("Fecha: ")
            consulta = Consulta(
                paciente,
                motivo,
                fecha
            )
            veterinaria.registrar_consulta(consulta)
        else:
            print("Paciente inexistente")
    elif opcion == "3":
        veterinaria.mostrar_historial()
    elif opcion == "4":
        veterinaria.calcular_ingresos_totales()
    elif opcion == "5":
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida")