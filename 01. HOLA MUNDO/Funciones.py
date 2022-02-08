# Funciones definieno un parametro

def funcion_1(name="Pepe"):
    print (f"hola {name}")

funcion_1()


# Funciones 2 con parametros fuera

def funcion_1(name):
    print (f"hola {name}")

funcion_1("Eduardo")
funcion_1("Pepe")

# Funciones 3 con varios parametros dentro

def funcion_1(name="Pepe",edad="22"):
    print (f"hola {name} y tu edad es {edad}")

funcion_1()

# Funciones 4 con varios parametros fuera

def funcion_1(name,edad):
    print (f"hola {name} y tu edad es {edad}")

funcion_1("Jose",48)

# funcion 5 con operacion de sumas externo

def sumar(a,b):
    return a+b
sum=sumar(23,45)
print (sum)
sum=sumar(43,43)
print (sum)

# funcion 5 con operacion de sumas interno

def sumar(a=24,b=33):
    return a+b
sum=sumar()
print (sum)

# funcion 6 con operacion de funcion recursiva

def recursiva (k):
    if (k > 0):
        resultado = 1 + recursiva (k-1)
        print (resultado)
    else:
        resultado = 0
    return resultado
recursiva (7)