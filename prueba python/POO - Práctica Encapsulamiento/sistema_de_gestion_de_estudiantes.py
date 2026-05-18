class Estudiante:
    def __init__(self, nombre, edad):
    # atributos privados
        self.__nombre = nombre
        self.__edad = edad
        self.__calificaciones = []
    #Métodos get
    def get_nombre(self):
        return self.__nombre
    def get_edad(self):
        return self.__edad
    #Métodos set
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("Edad inválida")
    #Manejo de calificaciones
    def agregar_calificacion(self, nota):
        if 0 <= nota <= 10:   #se puede cambiar escala si usan 0-100
            self.__calificaciones.append(nota)
        else:
            print("Calificación inválida")
    def calcular_promedio(self):
        if len(self.__calificaciones) == 0:
            return 0
        return sum(self.__calificaciones) / len(self.__calificaciones)
    def mostrar_calificaciones(self):
        return self.__calificaciones
alumno1 = Estudiante("Juan", 20)
print(alumno1.get_nombre())
print(alumno1.get_edad())
alumno1.agregar_calificacion(8)
alumno1.agregar_calificacion(9)
alumno1.agregar_calificacion(10)
print(alumno1.mostrar_calificaciones())
print("Promedio:", alumno1.calcular_promedio())
alumno1.set_edad(21)
print("Nueva edad:", alumno1.get_edad())