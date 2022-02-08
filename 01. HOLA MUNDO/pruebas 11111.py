# Declaración de Variables

clave = "condicional"
es_correcta = False  # variable para saber cuando la contraseña es correcta








# Programa
for i in range(3):
    clave_usuario = input("Ingrese la contraseña para ingresar: ") # solicitu de contraseña en pantalla

    if clave == clave_usuario:  # contraseña coincide con la almacenada
        print("La contraseña es correcta")
        print("Espere en linea hasta que se cargue la pagina de inicio")
        es_correcta = True
        break  # Termina con el ciclo para que no siga mostrando mensajes

if not es_correcta:
    print("la contraseña no es correcta")
    print(f"Su cuenta ha sido bloqueda")
    print(f"contacte con el administrador")
