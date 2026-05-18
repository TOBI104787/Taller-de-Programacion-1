class cliente:
    def __init__ (self):
        self.__codigo = 4321
    def getcodigo(self):
        return self.__codigo
persona = cliente()
#print(persona.__codigo)
print(persona.getcodigo())