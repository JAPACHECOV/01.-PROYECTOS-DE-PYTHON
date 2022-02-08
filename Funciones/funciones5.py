

def factorial(num): # un numero multiplicado por sus anteriores
    resultado = num # no se multiplica por 0
    for i in range(num-1,1,-1):
        resultado = resultado * i

    return (resultado)

print (factorial(45))
