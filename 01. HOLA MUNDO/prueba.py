# Declaración de Variables

contraseña1 = "condicional"
intentos = 0
i=2 # variable para visualizar los intentos resantes

# Programa

while intentos < 3:
    contraseña = input("Ingrese la contraseña para ingresar: ") # solicitu de contraseña en pantalla

    if contraseña1==contraseña: # contraseña coincide con la almacenada
        print("La contraseña es correcta")
        print("Espere en linea hasta que se cargue la pagina de inicio")
        intentos=23
    else:   # contraseña no coincide con la almacenada
        print("la contraseña no es correcta")
        print(f"le quedan {i} intentos")
    intentos += 1
    i -=1
if intentos == 3: # Intentos sobrepasados
    print(f"Su cuenta ha sido bloqueda")
    print(f"contacte con el administrador")