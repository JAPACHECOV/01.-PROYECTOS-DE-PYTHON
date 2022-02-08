# herencia múltiple

class Telefono:
    def __init__(self):
        pass
    def Llamar(self):
        print ("Llamando .....")
    def Ocupado(self):
        print("Ocupado .....")

class Camara:
    def __init__(self):
        pass
    def Fotografia(self):
        print ("Tomando fotos .....")

class Reproductor:
    def __init__(self):
        pass
    def Reproduce_musica(self):
        print ("Reproduciendo musica .....")
    def Reproduce_video(self):
        print ("Reproduciendo video .....")

# clase que las une todas y por eso es diferente
# esta clase convina todas las anteriores

class Smartphone (Telefono,Camara,Reproductor):
    def __del__(self):
        print ("Telefono apagado")


#Objeto

movil = Smartphone ()

# llamar a las otras clases

print (dir(movil)) # dir(objeto) devuelve un directorio con acciones que se pueden aplicar al objeto
print (movil.Fotografia())
print (movil.Llamar())