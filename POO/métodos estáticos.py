# métodos estaticos

# 2er metodo para crear objetos en Python

# la palabra reservada es @staticmethod

# este metodo puede ser llamado sin crear una isntancia de clase -  no se necesita el __init__
# no tiene acceso a atributos exteriores
# o llamar a otra funcion dentro de una clase

# ejemplo
import math
class Pastel: # clase
    def __init__(self,ingredientes,tamaño):  # constructor
        self.ingredientes = ingredientes
        self.tamaño = tamaño

    def __repr__(self):
        return (f'Pastel ({self.ingredientes},'f'{self.tamaño})')

    def area(self):
        return self.tamaño_area (self.tamaño)

    @staticmethod
    def tamaño_area (A):
        return A ** 2 * math.pi

nuevo_pastel = Pastel (['Harina','Leche','Chocolate'],4)

print (nuevo_pastel.ingredientes)
print (nuevo_pastel.tamaño)
print (nuevo_pastel.tamaño_area(12)) # este es un valor independiente solo funciona para el metodo estatico
# no para el resto



