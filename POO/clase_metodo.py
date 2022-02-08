class Matematica:
    def suma (self):
        self.n1 = 2
        self.n2 = 3


s = Matematica()
s.suma()
print (s.n1 + s.n2)

# otro metodo

class Ropa:
    def __init__(self):
        self.Marca= "Zara"
        self.Talla= "L"
        self.color = "Gris"

camisa = Ropa()
print (camisa.Talla)


class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto =n1 * n2
        self. division = n1/n2
operacion = Calculadora (2,3)
print (operacion.producto)
print (operacion.suma)


