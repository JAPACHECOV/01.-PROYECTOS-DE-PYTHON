# Condicionales anidadas

edad = int(input("digite su edad: "))

if edad>=18:
    print("Bienvenido a la pagina de inicio")
else:
    print("Usted no esmayor de edad y no puede entrar en la pagina")


edad = int(input("digite su edad: "))

if edad>0 and edad<100:
    if edad>18:
        print("Bienvenido a la pagina de inicio")
    else:
        print("Usted no esmayor de edad y no puede entrar en la pagina")
else:
    print("Dato erroneo")
    edad = int(input("Vuelva a digitar su edad: "))

edad = int(input("digite su edad: "))

if 0<edad<100:
    if edad > 18:
        print("Bienvenido a la pagina de inicio")
    else:
        print("Usted no esmayor de edad y no puede entrar en la pagina")
else:
    print("Dato erroneo")
    edad = int(input("Vuelva a digitar su edad: "))