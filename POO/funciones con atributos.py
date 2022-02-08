# funciones para atibutos

class Persona:
    edad =27
    nombre = "Victor"
    pais = "España"
doctor = Persona ()
print ("La edad es",doctor.edad)

print ("La edad es",getattr(doctor,"edad")) # otra forma mas directa

print ("El doctor tiene una edad?", hasattr(doctor, "edad")) # nos indica si el grupo al que pertenece doctor tiene ese atributo o no
print ("El doctor tiene un apellido?", hasattr(doctor, "apellido"))

print ("Su nombre era", doctor.nombre)
setattr(doctor,'nombre','Jose') # Cambia el valor del atributo
print ("Pero ahora su nombre es", doctor.nombre)

delattr(Persona,"pais") # borra un atributo de la clase
print (doctor.nombre)