
# como escribimos en el????

archivo_Leer = open("Leer_2.txt", "w") # abrir archivo y borrar el contenido si ya existe o crearlo de nuevo vacio
print(archivo_Leer.write("Este es un nuevo archivo \nY en el se escribira este texto")) # añade el texto entre comillas al archivo
# para añadir mas contenido se deberia de usar otro parametro
print(archivo_Leer.writable())# verifica que lo abrimos com W y es escribible
archivo_Leer.close() #cerrar un archivo
#Para añadir tenemos quecerrar y volver a abrir
archivo_Leer = open("Leer_2.txt", "a") # abrir archivo y añadir contenido

# como escribimos un adicional en el????

print(archivo_Leer.write("\nmi casa es bonita")) # añade el texto entre comillas al archivo
print(archivo_Leer.writable())# verifica que lo abrimos com W y es escribible
archivo_Leer.close() #cerrar un archivo

# Y para leer lo mismo, lo cerramo y lo volvemos a abrir

archivo_Leer = open("Leer_2.txt", "r") # abrir archivo y añadir contenido
print(archivo_Leer.read())# verifica que lo abrimos com W y es escribible
archivo_Leer.close() #cerrar un archivo