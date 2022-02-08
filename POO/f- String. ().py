# metodo f- String. ()

# Es otra forma mas eficiente de formar cadenas

# Recordar .format % y str.format

curso="Python"

print ("tutoriales de % s"%curso) # una variable

nombre="Victor"
edad=25

print ("Hola soy % s y tengo % s años"% (nombre,edad)) # varias variables

# str.format

print("Que tal, soy {} y mi edad es {} años.".format(nombre,edad))

# metodo f- String. () que es mas visual y legible

print(f"Hola soy {nombre} y mi edad es {edad}")

# ejercicio

class Estudiante:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self): # metodo de representacion informal de un objeto, esmas para visualizar
        return f"Hola que tal, soy {self.nombre} {self.apellido} y tengo {self.edad} años"

nuevo_estudiante= Estudiante('victor','cruz',17)
print(f"{nuevo_estudiante}")

# hay otro metodo repr (es mas formal y el nombre tiene un valor, no solo es para representar algo)

class Estudiante:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __repr__(self): # metodo de representacion informal de un objeto
        return f"Hola que tal, soy {self.nombre} {self.apellido} y tengo {self.edad} años"

nuevo_estudiante= Estudiante('victor','cruz',17)
print(f"{nuevo_estudiante !r}") # igual que el otro pero añadiendo !r

# el resultado es el mismo pero se repeta lo que reprenta los valores del objeto, es como mas completo y eso lo entiende python
# dentro del codigo.
