# métodos de clase

# 1er metodo para crear objetos en Python

# la palabra reservada es @classmethod

# este metodo puede ser llamado sin crear una isntancia de clase -  no se necesita el __init__
# no tiene acceso a atributos de instancia

# ejemplo

class Pastel: # clase
    def __init__(self,ingredientes):  # constructor
        self.ingredientes = ingredientes

    def __repr__(self):
        return f'Pastel ({self.ingredientes !r})'

    @classmethod
    def Pastel_chocolate (cls) :
        return cls (['Harina','Leche','Chocolate']) # se definen elementos de una clase pero son independientes, solo para pastel de chocolate

    @classmethod
    def Pastel_vainilla (cls) :
        return cls (['Harina','Leche','vainilla'])

print (Pastel.Pastel_chocolate())

