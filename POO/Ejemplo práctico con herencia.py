2# Ejemplo práctico con herencia

class Calculadora:
    def __init__(self,numeros):
        self.n = numeros
        self.datos = [ 0 for i in range (numeros)]

    def ingresardato (self):
        self.datos = [int(input('Ingresar datos: '+str(i+1)+ '= ')) for i in range(self.n)]

class Op_basicas (Calculadora):
    def __init__(self):
        Calculadora. __init__(self,2)

    def suma(self):
        a,b, = self.datos
        s = a+b
        print ('El resultado es:',s)

    def resta(self):
        a,b, = self.datos
        s = a-b
        print ('El resultado es:',s)

class Raiz (Calculadora):
    def __init__(self):
        Calculadora. __init__(self,1)

    def R_cuadrada (self):
        import math
        a, = self.datos
        print ("El resultado es: ",math.sqrt(a))

ejemplo = Op_basicas()
print (ejemplo.ingresardato())
print(ejemplo.suma())


ejemplo = Raiz()
print (ejemplo.ingresardato())
print(ejemplo.R_cuadrada())
