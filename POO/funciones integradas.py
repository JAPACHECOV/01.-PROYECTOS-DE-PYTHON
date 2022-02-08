# Ejemplo  funciones integradas

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


objeto = Op_basicas()

# primera funcion integrada isinstance. verifica la herencia

print(isinstance(objeto,Op_basicas))
print(isinstance(objeto,Raiz))

# Segunda funcion integrada isinstance. verifica la pertenencia de la subclase

print(issubclass(Calculadora,Op_basicas)) # al reves
print(issubclass(Op_basicas,Calculadora))
print(issubclass(Raiz,Calculadora))



