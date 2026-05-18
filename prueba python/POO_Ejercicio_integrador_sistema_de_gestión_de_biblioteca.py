#Clase base: Publicacion
class Publicacion:
    def __init__(self, titulo, autor, año_publicacion):
        #atributos privados
        self.__titulo = titulo
        self.__autor = autor
        self.__año_publicacion = año_publicacion
    #GETTERS
    def get_titulo(self):
        return self.__titulo
    def get_autor(self):
        return self.__autor
    def get_año_publicacion(self):
        return self.__año_publicacion
    #SETTERS
    def set_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo
    def set_autor(self, nuevo_autor):
        self.__autor = nuevo_autor
    def set_año_publicacion(self, nuevo_año):
        if nuevo_año > 0:
            self.__año_publicacion = nuevo_año
        else:
            print("Año inválido")
    #Método polimórfico
    def mostrar_info(self):
        print("Título:", self.__titulo)
        print("Autor:", self.__autor)
        print("Año de publicación:", self.__año_publicacion)
# Clase derivada: Libro
class Libro(Publicacion):
    def __init__(self, titulo, autor, año_publicacion, disponible):
        #uso de super()
        super().__init__(titulo, autor, año_publicacion)
        self.__disponible = disponible
    #Getter y Setter
    def get_disponible(self):
        return self.__disponible
    def set_disponible(self, estado):
        self.__disponible = estado
    # Método específico
    def verificar_prestamo(self):
        if self.__disponible:
            return "El libro está disponible para préstamo."
        else:
            return "El libro NO está disponible."
    # Polimorfismo
    def mostrar_info(self):
        super().mostrar_info()
        print("Disponible:", self.__disponible)
# Clase derivada: Revista
class Revista(Publicacion):
    def __init__(self, titulo, autor, año_publicacion, numero_edicion):
        super().__init__(titulo, autor, año_publicacion)
        self.__numero_edicion = numero_edicion
    #Getter y Setter
    def get_numero_edicion(self):
        return self.__numero_edicion
    def set_numero_edicion(self, nuevo_numero_edicion):
        self.__numero_edicion = nuevo_numero_edicion
    #Polimorfismo
    def mostrar_info(self):
        super().mostrar_info()
        print("Número de edición:", self.__numero_edicion)
# Clase derivada: Periodico
class Periodico(Publicacion):
    def __init__(self, titulo, autor, año_publicacion, fecha):
        super().__init__(titulo, autor, año_publicacion)
        self.__fecha = fecha
    #Getter y Setter
    def get_fecha(self):
        return self.__fecha
    def set_fecha(self, nueva_fecha):
        self.__fecha = nueva_fecha
    #Polimorfismo
    def mostrar_info(self):
        super().mostrar_info()
        print("Fecha:", self.__fecha)
#Programa principal
#Crear objetos
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, True)
revista1 = Revista("National Geographic", "Varios", 2024, 15)
periodico1 = Periodico("El Diario", "Redacción", 2025, "01/05/2025")
#Lista para mostrar polimorfismo
publicaciones = [libro1, revista1, periodico1]
#Mostrar información
for publicacion in publicaciones:
    print("\n-------------------")
    publicacion.mostrar_info()
#Método específico de Libro
print("\n", libro1.verificar_prestamo())