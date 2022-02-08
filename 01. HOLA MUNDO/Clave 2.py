# Ejercico 3 Clave

contraseñaR="condicional"

contraseña=input("por favor ingresa la contraseña: ")

if contraseña!=contraseñaR:
    for i in [3,2]:
        print("La contraseña es incorrecta")
        print(f"le quedan {i-1} intentos antes de bloquear su cuenta")
        contraseña = input("por favor ingresa de nuevo la contraseña correcta: ")

    print("La contraseña no es correcta")
    print("Ha agotado los 3 intentos de inicio de sesion")
    print("contacte con el administrador")

else:
    print("La contraseña es correcta")
