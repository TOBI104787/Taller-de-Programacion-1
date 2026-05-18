# =========================
# Clase Animal
# =========================

class Animal:

    def __init__(self, nombre, especie, edad, salud):

        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad
        self.__salud = salud


    # ===== GETTERS =====
    def get_nombre(self):
        return self.__nombre

    def get_especie(self):
        return self.__especie

    def get_edad(self):
        return self.__edad

    def get_salud(self):
        return self.__salud


    # ===== SETTERS =====
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_especie(self, nueva_especie):
        self.__especie = nueva_especie

    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad

    def set_salud(self, nueva_salud):
        self.__salud = nueva_salud


    # ===== Métodos =====
    def mostrar_info(self):

        print("Nombre:", self.__nombre)
        print("Especie:", self.__especie)
        print("Edad:", self.__edad)
        print("Salud:", self.__salud)


    def actualizar_salud(self, nueva_salud):
        self.__salud = nueva_salud
        print("Estado de salud actualizado")


# =========================
# Clase derivada
# =========================

class AnimalExotico(Animal):

    def __init__(
        self,
        nombre,
        especie,
        edad,
        salud,
        pais_origen,
        nivel_riesgo
    ):

        # Uso de super()
        super().__init__(nombre, especie, edad, salud)

        self.__pais_origen = pais_origen
        self.__nivel_riesgo = nivel_riesgo


    # ===== GETTERS =====
    def get_pais_origen(self):
        return self.__pais_origen

    def get_nivel_riesgo(self):
        return self.__nivel_riesgo


    # ===== SETTERS =====
    def set_pais_origen(self, nuevo_pais):
        self.__pais_origen = nuevo_pais

    def set_nivel_riesgo(self, nuevo_nivel):
        self.__nivel_riesgo = nuevo_nivel


    # ===== Polimorfismo =====
    def mostrar_info(self):

        # Método de la clase base
        super().mostrar_info()

        # Información extra
        print("País de origen:", self.__pais_origen)
        print("Nivel de riesgo:", self.__nivel_riesgo)


# =========================
# Clase Zoologico
# =========================

class Zoologico:

    def __init__(self, nombre, ubicacion):

        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__animales = []


    # ===== Agregar animal =====
    def agregar_animal(self, animal):

        self.__animales.append(animal)

        print("Animal agregado correctamente")


    # ===== Eliminar animal =====
    def eliminar_animal(self, nombre):

        for animal in self.__animales:

            if animal.get_nombre() == nombre:

                self.__animales.remove(animal)

                print("Animal eliminado")
                return

        print("Animal no encontrado")


    # ===== Buscar animal =====
    def buscar_animal(self, nombre):

        for animal in self.__animales:

            if animal.get_nombre() == nombre:
                return animal

        return None


    # ===== Mostrar animales =====
    def mostrar_animales(self):

        if len(self.__animales) == 0:

            print("No hay animales registrados")

        else:

            for animal in self.__animales:

                print("\n-------------------")

                # Polimorfismo
                animal.mostrar_info()
# Crear zoológico
zoo = Zoologico("Zoo Nacional", "Buenos Aires")


# Crear animales
animal1 = Animal(
    "Leo",
    "León",
    5,
    "Buena"
)

animal2 = AnimalExotico(
    "Kira",
    "Tigre Blanco",
    3,
    "Regular",
    "India",
    "Alto"
)


# Agregar animales
zoo.agregar_animal(animal1)
zoo.agregar_animal(animal2)


# Mostrar animales
print("\nLISTA DE ANIMALES")
zoo.mostrar_animales()


# Buscar animal
print("\nBUSCAR ANIMAL")

encontrado = zoo.buscar_animal("Kira")

if encontrado:
    encontrado.mostrar_info()
else:
    print("Animal no encontrado")


# Actualizar salud
animal1.actualizar_salud("Excelente")


# Eliminar animal
zoo.eliminar_animal("Leo")


# Mostrar nuevamente
print("\nLISTA ACTUALIZADA")
zoo.mostrar_animales()