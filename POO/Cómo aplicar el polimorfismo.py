# Cómo aplicar el polimorfismo

# 3 formas de aplicarlo

# 1 polimorfismo por funcion

class Tomate:
    def tipo (self):
        print('El tomate es un vegeral')
    def color (self):
        print('El tomate es Rojo')

class Manzana:
    def tipo(self):
        print('La Manzana es una Fruta')
    def color(self):
        print('La Manzana es Roja')

# Hay polimorfismo

def funcion(objeto):
    objeto.tipo()
    objeto.color()

nuevo_tomate = Tomate()
funcion(nuevo_tomate)

nuevo_manzana = Manzana()
funcion(nuevo_manzana)


# 1 polimorfismo con metodos
# (funciona bien cuando hay mas de 2 clases, es muy efectivo)

class España:
    def Capital (self):
        print ('Madrid')
    def Idioma (self):
        print ('Castellano')

# segunda clase ppolimorfismo or metodo

class Francia:
    def Capital (self):
        print ('Paris')
    def Idioma (self):
        print ('Frances')

# Llamamos los elementos

español = España()
frances = Francia()

# declaro los objetos para este polimorfismo por metodo

for pais in (español,frances):
    pais.Capital()
    pais.Idioma()

# tercera clase con herencia

class Aves:
    def volar(self):
        print('La mayoria de las aves pueden volar, pero algunas no')

class Aguila (Aves):
    def volar(self):
        print('Las aguilas pueden volar')

class Gallina (Aves):
    def volar(self):
        print('Las Gallinas no pueden volar')

obj_ave = Aves ()
obj_aguila = Aguila()
obj_gallina = Gallina()

obj_ave.volar()
obj_aguila.volar()
obj_gallina.volar()

# polimorfismo vincula objetos de forma mas efectiva