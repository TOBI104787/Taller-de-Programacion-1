#Clase base:
class empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
#Clase derivada:
class gerente(empleado):
    def __init__(self, nombre, salario, departamento):
        #Atributo propio de Gerente
        self.departamento = departamento
        #Usamos super() para llamar al constructor de Empleado
        super().__init__(nombre, salario)
    def mostrar(self):
        return f"gerente: {self.nombre} {self.salario} {self.departamento}"
el_gerente = gerente("nombre: Juan", "salario: 6000", "departamento: recursos humanos")
print(el_gerente.mostrar())