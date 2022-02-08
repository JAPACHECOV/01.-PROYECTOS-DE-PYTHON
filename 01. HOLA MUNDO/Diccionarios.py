# Dicionarios

Diccionario={1:"uno",2:"dos",3:"tres"}

# salida de datos

print (Diccionario)
print (Diccionario[1])
print (Diccionario[2])

# incluir datos

Diccionario [4] = "cuatro"

print (Diccionario)

# Borrar datos

del (Diccionario[1])

print (Diccionario)

# Diccionarios o listas dentro de diccionarios ejemplo agenda

Diccionario={"Pacheco":[1.93,78,48],"Glenda":[1.70,"No preguntes","Esto menos"] }

print (Diccionario)

Diccionario={"Pacheco":{"estatura":1.93,"peso":78,"edad":48},"Glenda":{"estatura":1.70,"peso":"No preguntes","edad":"Esto menos"}}

print (Diccionario)


# Crear un diccionario

equipo={10:"Messi",16:"Pedri",6:"Busquets",1:"Zubizarreta"}

print (equipo)
print (equipo[10])

# imprimir un valor que no esta pero que no salga error

print(equipo.get(9,"No existe ese jugador en el equipo"))

# comprobar si un valor esta

print (10 in equipo) # True
print (9 in equipo) # False

# imprimir solo claves

print (equipo.keys())

# imprimir solo valores

print (equipo.values())

# imprimir solo Items

print (equipo.items())

# Contar elementos

print (len(equipo))

# eliminar todos los elementos

equipo.clear()

print (equipo)
