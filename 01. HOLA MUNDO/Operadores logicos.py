# ejercicio operadores logicos

a = 10
b = 12
c = 13
d = 10

resultado=((a>b) or (a<c))and((a==c) or(a>=b))

print (resultado)

# ejercicio 2

a = 10
b = 15
c = 20

# paso 1

resultado=((a<b) and (b<c))

print (resultado)

# paso 2

resultado=((a>b) and (b<c))

print (resultado)

# paso 3

resultado=((a>b) or (b<c))

print (resultado)

# paso 3

resultado=not((a>b) or (b<c))

print (resultado)