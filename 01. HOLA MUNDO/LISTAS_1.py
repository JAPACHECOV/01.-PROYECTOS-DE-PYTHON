smartphones = ["Xiaomi", "Iphone","Huawei","Samsung"]

#imprimir en orden directo

print (smartphones [0])
print (smartphones [1])
print (smartphones [2])
print (smartphones [3])

#Imprimir en orden inverso (desde el final)

print (smartphones [-1])
print (smartphones [-2])
print (smartphones [-3])
print (smartphones [-4])

#Eliminar elementos de una lista

del (smartphones [1]) # elimina el segundo elemento
print (smartphones)

del (smartphones [-1]) # elimina el ultimo elemento
print (smartphones)

smartphones.remove("Huawei") # elimina el elemento por el nombre
print (smartphones)

# Añadir elemento a una lista al final

smartphones.append("Huawei") # anade Huawei al final
smartphones.append("Iphone") # anade Iphone al final
smartphones.append("Samsung") # anade Samsung al final

print (smartphones)

# Añadir elemento a una lista en una posicion especifica

smartphones.insert(1,"Oppo") # anade OPPO en poscion 2

print (smartphones)

smartphones.insert(-2,"Oneplus") # anade OPPO en poscion antepenultima

print (smartphones)