# Definición de variables

colores = [] # Lista
i=1 # Contador

# entrada de nombres de colores sin repetición

while i<=5:
    color = input("Añade el nombre de un color a tu lista: ") # añade un nuevo color al final
    while color in colores:
        print(f"El color {color} ya existe en la lista")
        color = input("Añade el nombre de un color a tu lista: ")
    colores.append(color)
    i += 1
print ()
print (f'Tu lista de colores es la siguiente: {colores}')
print ()

# añadir o borrar 1 color según si ya está en la lista o no lo está

print ('¿Quieres añadir o borrar un color en tu lista?')
elegir= input ('Digita (s) si o (n) no: ')

while elegir == 's':
    color = input('Digita el nombre del color que quieres añadir/borrar: ')
    if color in colores:
        colores.remove(color)
        print (f'Has borrado el color {color} de tu lista')
    else:
        colores.append(color)
        print(f'Has agregado el color {color} a tu lista')
    print(f'Tu nueva lista de colores es la siguiente: {colores}')
    print('¿Quieres añadir o borrar un color en tu lista?')
    elegir = input('Digita (s) si o (n) no: ')

if elegir=='n':
    print()
    print(f'Tu lista de colores final es la siguiente: {colores}')
    print()
    print("Fin del programa")


