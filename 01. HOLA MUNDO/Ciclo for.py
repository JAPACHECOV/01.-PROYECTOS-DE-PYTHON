# Ciclo for 1

for i in (1,2,3,4,"Jose"):
    print (f"Hola Mundo",i)

# Ciclo for 2 clave nombre

coleccion = {"Jose":48,"Glenda":45}

for i in (coleccion):
    print (f"Hola Mundo,{i}")

# Ciclo for 3 valor edad

coleccion = {"Jose":48,"Glenda":45}

for i in (coleccion):
    print (f"{coleccion[i]}")

# Ciclo for 4 los 2

coleccion = {"Jose":48,"Glenda":45}

for i in (coleccion):
    print (f"{i} --> {coleccion[i]}")

# Ciclo for 5 los 2 alternativo y profesional

coleccion = {"Jose":48,"Glenda":45}

for clave,valor in coleccion.items():
    print (f"{clave} --> {valor}")

# Ciclo for 6 Cadenas letra a letra

coleccion = "Jose"

for i in coleccion:
    print (f"{i}",end=" ")