#Clase base
class empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Salario:", self.salario)
#Clase derivada
class gerente(empleado):
    def __init__(self, nombre, salario, departamento):
        #Llamamos al constructor de la clase base
        super().__init__(nombre, salario)
        #Atributo propio de Gerente
        self.departamento = departamento
    def mostrar_info_completa(self):
        #Reutilizamos el método de Empleado
        super().mostrar_info()
        #Información adicional
        print("Departamento:", self.departamento)
gerente1 = gerente("Carlos", 5000, "Recursos Humanos")
gerente1.mostrar_info_completa()