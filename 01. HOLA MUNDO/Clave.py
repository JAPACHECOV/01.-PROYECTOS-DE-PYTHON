# Ejercico 3 Clave

contraseñaR="1"

intentos=0
i=2

while intentos<2:
    contraseña = input("Por favor ingresa la contraseña: ")
    if contraseñaR==contraseña:
        print("La contraseña es correcta")
        print("Espere en linea hasta que se cargue la pagina de inicio")
        break
    else:
        print(intentos)
        print(i)
        print("La contraseña es incorrecta")
        print(f"le quedan {i} intentos antes de bloquear su cuenta")
    intentos += 1
    i -= 1
if intentos<3:
    print (intentos)
    print(f"le quedan 0 intentos")
    print(f"Su cuenta ha sido bloqueda")
    print(f"contacte con el administrador")