# Definicion de variables

colores = []
i=1
# elegir="n"

# entrada de nombres de colores sin repeticion

while i<=5:
    color = input("anade el nombre de un color: ") # anade un nuevo color al final
    print (color)
    print (colores)
    while color in colores:
        print(f"El color {color} ya existe en la lista")
        color = input("anade el nombre de un color: ")
    colores.append(color)
    print(colores)
    i += 1
print ()
print (f'Tu lista de colores es la siguiente: {colores}')
print ()

# elegir = input("Digite (a) para AÑADIR o (b) para BVORRAR un color de su lista. Si NO desea modificarla digite (n):  ")
# print ("primer imput")

#while elegir != "a" or elegir != "b" or elegir != "a":
#    while elegir == 'a':
#        colores.append(input("anade el nombre de un color a añadir: "))  # anade otro color al final
#        print(f'Has añadido el color {colores[-1]} a tu Lista de colores')
#        print(f'Tu nueva lista de colores es la siguiente: {colores}')
#        break
#    while elegir == 'b':
#        borrado = input("anade el nombre de un color a borrar: ")  # Borra un color especificado
#        colores.remove(borrado)  # Borra un color especificado
#        print(f'Has borrado el color {borrado} a tu Lista de colores')
#        print(f'Tu nueva lista de colores es la siguiente: {colores}')
#        break
#    while elegir == 'n':
  #      print()
 #       print(f'Tu lista de colores final es la siguiente: {colores}')
#       print()
#        print("fin del prrograma")
#        break
# elegir = input("Digite (a) para AÑADIR o (b) para BVORRAR un color de su lista. Si NO desea modificarla digite (n):  ")
# print("segundo imput")

elegir = 2

while elegir != "a" and elegir != "b" and elegir != "n":
    elegir = input("Digite (a) para AÑADIR o (b) para BVORRAR un color de su lista. Si NO desea modificarla digite (n):  ")
    print("segundo imput")
    print (elegir)

    if elegir == 'a':
        colores.append(input("anade el nombre de un color a añadir: "))  # anade otro color al final
        print(f'Has añadido el color {colores[-1]} a tu Lista de colores')
        print(f'Tu nueva lista de colores es la siguiente: {colores}')

    elegir = input("Digite (a) para AÑADIR o (b) para BVORRAR un color de su lista. Si NO desea modificarla digite (n):  ")
    print("cuarto imput")
    print(elegir)

    if elegir == 'b':
        borrado = input("anade el nombre de un color a borrar: ")  # Borra un color especificado
        colores.remove(borrado)  # Borra un color especificado
        print(f'Has borrado el color {borrado} a tu Lista de colores')
        print(f'Tu nueva lista de colores es la siguiente: {colores}')

    elegir = input("Digite (a) para AÑADIR o (b) para BVORRAR un color de su lista. Si NO desea modificarla digite (n):  ")
    print("Quinto imput")
    print(elegir)

    if elegir == 'n':
        print()
        print(f'Tu lista de colores final es la siguiente: {colores}')
        print()
        print("fin del prrograma")

    elegir = input("Digite (a) para AÑADIR o (b) para BVORRAR un color de su lista. Si NO desea modificarla digite (n):  ")
    print("tercer imput")
    print(elegir)