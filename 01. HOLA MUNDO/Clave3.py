# Ejercico 3 Clave

contraseñaR="1"

contraseña=input("por favor ingresa la contraseña: ")

i=2
intentos=0

while i>0 or intentos<3:

    if contraseñaR!=contraseña:
        print(i)
        print(intentos)
        print("La contraseña es incorrecta")
        print(f"le quedan {i} intentos antes de bloquear su cuenta")
        contraseña = input("por favor ingresa de nuevo la contraseña correcta: ")
        if intentos==2:
            print(f"le quedan {i-1} intentos")
            print(f"Su cuenta ha sido bloqueda")
            print(f"contacte con el administrador")
        i -= 1
        intentos += 1

    else:
        print("La contraseña es correcta")
        print("Espere en linea hasta que se cargue la pagina de inicio")
        i = -2