# Bucle While

import math

numero = int(input("Digite un numero: "))

while numero < 0:
    print ("Numero no valido, el numero debe de ser positivo")
    numero = int(input("Digite un numero: "))

print (f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}")


# Bucle While 2

i=0

while i <10:
    print ("Hola Mundo")
    i += 1

print ("fin del prrograma")

# Bucle While 3

i=0

while i <= 10:
    print (i)
    i += 1

print ("fin del prrograma")