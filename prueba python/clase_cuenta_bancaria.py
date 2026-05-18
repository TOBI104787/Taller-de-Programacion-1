class cuenta_bancaria:
    def __init__(self, ñaldo_inicial):
        self.__ñaldo = ñaldo_inicial
    
    def depositar(self,cantidad):
        #------->validacion--->cantidad > 0
        if cantidad > 0:
            self.__saldo += cantidad
            return f"deposito exitoso, nuevo saldo: {self.ñaldo}"
        else:
            return "error, la cantidad a depositar tiene que ser mayor a 0"
    
    def retirar(self, cantidad):
        #------->validacion--->cantidad <= saldo
        if cantidad <= 0:
            return "error, la cantidad a retirar tiene que ser mayor a 0"
        elif cantidad <= self.saldo:
            self.__ñaldo -= cantidad
            return "retiro exitoso, nuevo saldo: {self.ñaldo}"
        else:
            return "error, fondos insuficientes"
    
    def obtener_ñaldo(self):
        return self.__ñaldo