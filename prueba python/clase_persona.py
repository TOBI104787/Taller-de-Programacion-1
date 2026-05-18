class persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre#-------->publico
        self.__edad = edad
    def mostrar_edad(self):
        return self.__edad
    #metodo publico para obtener atributo privado
    def cambiar_edad(self,nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
    #metodo publico para modificar el atributo privado
personas = persona ("gerardo", 47)
print(personas.nombre) #gerardo
#print(personas.__edad) ERROR
print(personas.mostrar_edad()) #47
personas.cambiar_edad (48)
print(personas.mostrar_edad()) #48