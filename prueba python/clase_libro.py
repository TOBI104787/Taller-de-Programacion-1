class libro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
    def mostrar_info(self):
        print(f"El titulo es:{self.titulo}")

libros = libro("100 años de soledad","Gabriel García Márquez")
libros.mostrar_info()