class pato:
    def __init__ (self):
        pass
    def animal(self):
        print("pato")
class perro:
    def __init__ (self):
        pass
    def caminar(self, accion):
        print(f"puede caminar{accion}")
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
class animal(pato, perro, pez, pajaro):
    def __init__ (self):
        print("animal")
pato = animal()
pato.animal()
pato.caminar(" y saltar")
pato.nadar()
pato.volar()