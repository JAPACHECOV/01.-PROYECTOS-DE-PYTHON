# solicitud de variables

print("Valores a operar")
print(" ")
num1 = float(input("Digite primer número: "))
num2 = float(input("Digite segundo número: "))
print(" ")

# solicitud de operación

print(" ")
print ("Elija el tipo de operación")
print ("    Sumar (+) ")
print ("    Restar (-) ")
print ("    multiplicar (x) ")
print ("    Dividir (/) ")

operacion = input("Digite un valor valido para la operación (+, -, x, /):  ")

# ejecución de la operación seleccionada

if operacion!="+":
    if operacion!="-":
        if operacion!="x":
            if operacion!="/":
                print("El valor de la operación digitada no es válido")
                operacion = input("Digite de nuevo un valor valido para la operación (+, -, x, /):  ")

if operacion == "+":
    resultado = num1+num2
    Operacion1= "suma"
else:
    if operacion == "-":
        resultado = num1-num2
        Operacion1 = "resta"
    else:
        if operacion == "x":
            resultado = num1*num2
            Operacion1 = "multiplicación"
        else:
            if operacion == "/":
                resultado = num1/num2
                Operacion1 = "división"

# Resultados

print(" ")
print(" ")
print(f"Ejemplo: {Operacion1}")
print(f"{num1}{operacion}{num2}")
print(f"Resultado: {resultado}")


