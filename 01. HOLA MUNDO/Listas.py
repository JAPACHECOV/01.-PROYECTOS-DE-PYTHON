# Definicion de variables

colores = []
i=1

# entrada de nombres de colores

while i <=5:
    colores.append(input("anade el nombre de un color: ")) # anade un nuevo color al final)
    i += 1
print ()
print (f'Tu lista de colores es la siguiente: {colores}')
print ()
print ()
elegir=input ("Digite (a) para AÑADIR o (b) para BVORRAR un color de su lista. Si NO desea modificarla digite (n):  ")

# Programa de añadir o borrar algun dato

while elegir != "no":
    while elegir=='a':
        colores.append(input("anade el nombre de un color a añadir: ")) # anade otro color al final
        print(f'Has añadido el color {colores[-1]} a tu Lista de colores')
        print(f'Tu nueva lista de colores es la siguiente: {colores}')
        elegir=input ("Digite (a) para AÑADIR o (b) para BVORRAR un color de su lista. Si NO desea modificarla digite (n):  ")
    while elegir == 'b':
        borrado=input("anade el nombre de un color a borrar: ") # Borra un color especificado
        colores.remove(borrado)  # Borra un color especificado
        print(f'Has borrado el color {borrado} a tu Lista de colores')
        print(f'Tu nueva lista de colores es la siguiente: {colores}')
        elegir=input ("Digite (a) para AÑADIR o (b) para BVORRAR un color de su lista. Si NO desea modificarla digite (n):  ")
    print("La respuesta no es valida")
    elegir = input("Digite (a) para AÑADIR o (b) para BVORRAR un color de su lista. Si NO desea modificarla digite (n):  ")

else:
    print()
    print(f'Tu lista de colores final es la siguiente: {colores}')
    print()
    print("fin del prrograma")


