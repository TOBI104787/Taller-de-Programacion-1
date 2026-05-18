class calculadora:
    def __init__(self,N1,N2):
        self.N1 = N1
        self.N2 = N2
        
    def suma(self):
        print(self.N1+self.N2)
        
    def resta(self):
        print(self.N1-self.N2)
        
    def multiplicar(self):
        print(self.N1*self.N2)
        
    def dividir(self):
        print(self.N1/self.N2)

calculo = calculadora(10, 5)
calculo.suma()
calculo.resta()
calculo.multiplicar()
calculo.dividir()