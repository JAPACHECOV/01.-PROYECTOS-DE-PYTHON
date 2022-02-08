# Primero se crea la raiz, ventana donde estan losbotones priccipales, maximizar cerrar etc ...
# dentro de la ventana se construye el frame y es lo que interactua con el usuario


# la raiz se importa de la libreria tkinter

from tkinter import *


raiz=Tk() # se define raiz en la libreria

# metodos que definen las caracteristicas de mi ventana

raiz.title ("Ventana inicial") # metodo que define el titulo
raiz.resizable(True, True) # metodo para no dejar o si dejar que se puedamodificar el tamaño de la ventana (premer false ancho, segundo false alto
raiz.iconbitmap("Images/conagea.ico") # metodo para cambiar la imagen de la ventana con una imagen .ico (siempre)
raiz.geometry ("850x650") # le da el tamaño inicial que nosotros deseemos
raiz.config(bg="green")# cambia el color, hay diferentes parametros que podemos configurar

# metodo que va al final

raiz.mainloop () # se define el metodo mainloop esto siempre va lo ultimo

