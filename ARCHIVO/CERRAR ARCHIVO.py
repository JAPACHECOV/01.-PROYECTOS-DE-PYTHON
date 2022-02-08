

archivo_Leer = open("Leer_3.txt", "w") # abrir archivo y añadir contenido
print(archivo_Leer.write("Hola"))# verifica que lo abrimos com W y es escribible
archivo_Leer.close() #cerrar un archivo

# Eliminar un archivo
# se hace con una libreria
# sellama al modulo OS

import os

os.remove("Leer_3.txt") # esto lo elimina

