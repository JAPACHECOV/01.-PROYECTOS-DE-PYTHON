# Polimorfismo
# una subclase cuanta con metodos con el mismo nombres
# La clase superior define comportamientos diferentes
# se define polimorfismo como:
# Capacidad que tiene los objetos en diferentes clasespara usar un
# comportamiento o atributo del mismo nombre pero con diferente valos

#ejemplo

class Auto:  # defino clase
    rueda = 4  # defino un objeto en la clase
    def desplazamiento (self):
        print ("El auto se esta desplazando sobre 4 ruedas")


class Moto:  # defino clase
    rueda = 2  # defino un objeto en la clase diferente pero con desplazamiento en comun
    def desplazamiento(self):
        print("La Moto se esta desplazando sobre 2 ruedas")

# ambas clases tienen la capacidad de desplazarse, pero de diferente forma

# Hay todo tipo de polimorfismo

class Animales:
    def __init__(self,nombre):
        self.nombre =nombre

    def tipo_animal (self):
        pass

class Leon(Animales):
    def tipo_animal(self):
        print ('Animal Salvaje')

class Perro(Animales):
    def tipo_animal(self):
        print ('Animal Domestico')


nuevo_animal = Leon ('SIMBA')
nuevo_animal.tipo_animal()

nuevo_animal = Perro ('BOBY')
nuevo_animal.tipo_animal()

# mismo nombre del metodo pero no cumplen la misma accion

