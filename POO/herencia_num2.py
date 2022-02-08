# Problema:
#
# Herencia
#
# Realizar un programa que conste de una clase Persona con dos atributos nombre y edad. Los atributos se introducirán por teclado
# y habrá otro método para imprimir los datos.
#
# Declarar una segunda clase llama Empleado que hereda de la clase Persona y agrega el atributo sueldo. Debe mostrar si tiene que pagar
# impuestos o no (sueldo superior a 3000).
# Crear un objeto de cada clase.

# inicio del programa

v='s'

# bucle para reiniciar el programa

while v=='s' or v=="S":

# definicion Clase Persona

    class Persona:
        pass
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad
        def descripcion(self):
            return 'El nombre de la persona introducido es {} y {} tiene una edad de {} años'.format(self.nombre,
                                                                                                     self.nombre,
                                                                                                     self.edad)
# Clase Empleado que hereda Persona

    class Empleado(Persona):
        def valor_del_sueldo(self, sueldo):
            return 'El nombre del empleado es {} y {} tiene un sueldo de {} dolares'.format(self.nombre,
                                                                                                         self.nombre,
                                                                                                         sueldo)
        def pagar_impuestos(self, sueldo):
            if (sueldo > 3000):
                return '{} tiene que pagar impuesto ya que su sueldo de {} es mayor del limite minimo establecido por HACIENDA de 3000 $'.format(
                    self.nombre, sueldo)
            else:
                return 'Enhorabuena {} no tiene que pagar impuestos'.format(self.nombre)

# Introduccion de parametros

    n = input('Ingresar nombre de la Persona: ')
    e = int(input('Ingresar la edad de la Persona: '))
    while e < 18:
        if 0 < e < 18:
            print("ERROR, edad no valida para un empleado legal")
            e = int(input('Vuelva a ingresar una edad correcta (+18 años): '))
        if e <= 0:
            print("ERROR, edad no valida PARA UN SER VIVO")
            e = int(input('Vuelva a ingresar una edad correcta (+18 años): '))
    s = int(input('Ingresar el sueldo que cobra la Persona: '))
    while s < 300:
        if 0 < s < 300:
            print("ERROR, TE ESTAN EXPLOTANDO")
            s = int(input('Ingresar un valor de sueldo valido para un empleado legal: '))
        if s <= 0:
            print("ERROR, SUELDO NO VALIDO")
            s = int(input('Ingresar un valor de sueldo valido: '))

# Objeto_1 Clase Persona

    print()
    print('Objeto de clase Persona')
    nueva_persona = Persona(n, e)
    print(nueva_persona.descripcion())

# Objeto_1 Clase Empleado

    print()
    print('Objeto de clase Empleado')
    nueva_persona = Empleado(n, e)
    print(nueva_persona.valor_del_sueldo(s))
    print()
    print(nueva_persona.pagar_impuestos(s))
    print()


# fin del programa
# bucle para reiniciar

    v=input('Quiere volver a ejecutar la funcion, presione "s" (Si) o "n" (No): ')
    if v!='n' and v!='N' and v!='s' and v!='S':
        print ('valor erroneo')
        print ('tiene que usar "s" o "S" para (Si) o "n" o "N" para (no).')
        v = input('Vuelva a elegir una opcion valida? (s/n): ')
if v=='n' or v=="N":
    print('Gracias por participar')

# Fin del codigo