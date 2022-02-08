# importar de una libreria ya existente llamada Ramdon
# a puedes colocar dentro de la misma carpeta de tus archivos del programa

from random import *

def generarNumeroAleatorio(min, max):
    try:
        if min > max: # loop para cambiar max por minimo si se entran al reves
            aux = min
            min = max
            max = aux
        return randint (min, max)
    except TypeError:
        print ("Debes escribir numeros")
        return -1
i=0
while i<5:
    print (generarNumeroAleatorio(23, 10))
    i += 1