class animal:
    def __init__ (self):
        pass
    def animal(self):
        print("es un animal")
class perro:
    def __init__ (self):
        pass
    def caminar(self):
        print("puede caminar")
class pez:
    def __init__ (self):
        pass
    def nadar(self):
        print("puede nadar")
class pajaro:
    def __init__ (self):
        pass
    def volar(self):
        print("puede volar")
class pato(animal, perro, pez, pajaro):
    def __init__ (self):
        print("pato")
animal = pato()
animal.caminar()
animal.nadar()
animal.volar()