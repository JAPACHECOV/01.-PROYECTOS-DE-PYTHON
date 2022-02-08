

# Abrir o cerra archivos

archivo_Leer = open("Leer.txt", "r")  #Abrir un archivo
#Donde la letra adicional indica:

# \n Salto de linea
# "r" leer
# "r+" leer y escribir, pero sobre escribe el contenido
# "w" editar y escribir pero no leer y crea un archivo nuevo    que borra lo que habia antes
# "w+" editar y escribir y leer y crea un archivo nuevo y que borra lo que habia antes
# "lt" si es escritura o lectura
# "a" agregar no permite leer

# Ordenes sobrearchivos

print(archivo_Leer.readable()) # nos muestra si es verdaero o falso la exixtencia de un archivo que es leible
print(archivo_Leer.writable()) # nos da falso por que solo es leible no escribible

# print(archivo_Leer.read()) # lee e contenido del archivo

# print(archivo_Leer.readline()) # lee e contenido de la primera linea del archivo
# print(archivo_Leer.readline()) # si añadp otro lee la segunda linea

# print(archivo_Leer.readlines()) # devuelve una lista  por que lo toma como esto
# print(archivo_Leer.readlines()[2])

# IMPORTANTE cuando habro y leo un archivo, o alguna parte y luego lo vuelvo a leer, las partes que ya estaban leidas no aparecen en el segundo print

# print(archivo_Leer.readlines()[1])
# print(archivo_Leer.readlines()) # en este read no aparece pepe por que ya lo leyo en el readlines anterior. Para volvera leer hay que cerrar el archivo y volverlo a abrir
for est in archivo_Leer:
    print (est)

print(archivo_Leer.readlines()) # este saldra vacio
archivo_Leer.close() #cerrar un archivo

archivo_Leer = open("Leer.txt", "r")
print(archivo_Leer.readlines()) # este volvera a leerlos todos
archivo_Leer.close() #cerrar un archivo