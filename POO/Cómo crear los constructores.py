# construyendo constructores

class Persona:
    pass
    def __init__(self,nombre,año):
        self.nombre = nombre
        self. año = año   # metodo del constrctor

    def descripcion (self):
        return " {} Tiene {} años".format(self.nombre,self.año)

    def comentario (self, frase):
        return " {} dijo {} ".format(self.nombre,frase) # añade un atributo

doctor = Persona("Jose", 26)
print (doctor.nombre)
print (doctor.descripcion())
print (doctor.comentario("Hola que tal"))

# Modificar una atributo

class Email:
    def __init__(self):
        self.enviado=False
    def enviar_correo (self):
        self.enviado=True

mi_correo = Email ()

print (mi_correo.enviado)

mi_correo.enviar_correo()
print (mi_correo.enviado)