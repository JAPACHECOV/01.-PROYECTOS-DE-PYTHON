
from tkinter import *
from tkinter import messagebox #importar libreria de ventanas emergentes informativas o de eleccion
from tkinter import filedialog # abre una ventana de dialogo, se puede introducir informacion

def infoAdicional():  #libreria de ventanas emergentes funcion de actuaciones
    messagebox.showinfo("Programa de Pacheco", "Programa del 2019") # este parametro tiene 2 entradas la de arroba a la izquierda y la del centro
                                                                                # hay que asignarlo a algun elemento del programa
def infoLicencia():
    messagebox.showwarning("Licencia", "Licencia valida hasta el 2023")

def salirApp():

#    valor=messagebox.askquestion("Salir", "¿Esta seguro que quiere salir?") # para valor si o no
#    if valor=="yes":
    valor=messagebox.askokcancel("Salir", "¿Esta seguro que quiere salir?")  # funciona con verdadero y falso
    if valor==True:
        raiz.destroy()

def cerrarDoc():
    valor=messagebox.askretrycancel("Reintentar", "Cerra el documento")
    if valor==False:
        raiz.destroy()

def abreAcrh():
    archivo=filedialog.askopenfilenames(title="Abrir", initialdir="/",filetypes=(("Fichero de Excel","*xlsx"), ("Fichero de Texto","*txt"), ("Todos los ficheros","...")))
    print (archivo)

raiz=Tk()

miFrame=Frame(raiz, width=800, height=400)
miFrame.pack ()

miNombre=StringVar()
opcion=IntVar()

cuadroNombre=Entry(miFrame, textvariable=miNombre)
# cuadroTexto.place (x=100,y=100) # lo posiciona en coordenadas
cuadroNombre.grid (row=1, column=1, padx=20, pady=10) # lo posiciona en filas columnas
cuadroNombre.config (fg="red" , justify = "center")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid (row=2, column=1, padx=20, pady=10)
cuadroApellido.config (fg="blue" , justify = "left")

cuadroEdad=Entry(miFrame)
cuadroEdad.grid (row=3, column=1, padx=20, pady=10)
cuadroEdad.config (fg="green" , justify = "right")

cuadroPass=Entry(miFrame)
cuadroPass.grid (row=4, column=1, padx=20, pady=10)
cuadroPass.config (fg="blue" , justify = "left")
cuadroPass.config(show="*")

cuadroComentario=Text(miFrame,width=16, height=5) # tamaño de la ventana y se define como # Text
cuadroComentario.grid (row=5, column=1, padx=20, pady=10) #posicion de la ventana
scrollVertical=Scrollbar(miFrame, command=cuadroComentario.yview) # define el tipo de scrooll, vertical (V) u  horizontal (X)
scrollVertical.grid (row=5, column=2, sticky="nsew")  # posicionado se scroll
cuadroComentario.config (yscrollcommand=scrollVertical.set) # contola el posicionado de la barrita de scroll

# show = ocultar el texto con un caracter predefinido

nombreLabel=Label(miFrame, text="Nombre: ")
# nombreLabel.place (x=100,y=100) # lo posiciona en coordenadas
nombreLabel.grid (row=1, column=0, sticky="e", padx=20, pady=10) # lo posiciona en filas columnas

# sticky = alineacion segun puntos cardinales
# padx = Espacia los elementos, separa la caja de los nombres (horizontal)
# pady = Espacia los elementos, separa folas (vertical)


apellidoLabel=Label(miFrame, text="Apellidos: ")
apellidoLabel.grid (row=2, column=0, sticky="e", padx=20, pady=10)

edadLabel=Label(miFrame, text="Edad: ")
edadLabel.grid (row=3, column=0, sticky="e", padx=20, pady=10)

passLabel=Label(miFrame, text="Password: ")
passLabel.grid (row=4, column=0, sticky="e", padx=20, pady=10)

comentarioLabel=Label(miFrame, text="Comentarios: ")
comentarioLabel.grid (row=5, column=0, sticky="e", padx=20, pady=10)

def codigoBoton(): # definimos la fincion para enviar
    miNombre.set("Pacheco")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack ()

# Botones de accion/ eleccion

def imprimir():
    if opcion.get() ==1:
        etiqueta.config(text="Has elegido Masculino")
    else:
        etiqueta.config(text="Has elegido Femenino")

Label(raiz, text="Seleccione su Genero").pack() # lo imprime en la consola
Radiobutton(raiz,text="Maculino", variable=opcion, value=1, command=imprimir).pack () # para poder elegir
Radiobutton(raiz,text="Femenino", variable=opcion, value=2, command=imprimir).pack ()

etiqueta=Label(raiz)
etiqueta.pack()

#MENUS

barraMenu=Menu(raiz)
raiz.config(menu=barraMenu,width=300, height=300) #se establece el menu con la variable menu

# Se establecen los elementos que tendra el Menu

ArchivoMenu=Menu(barraMenu, tearoff=0)

# tearoff  -->  Borra una linea que sale por defecto en el submenu

# Se establecen los subelementos que tendra el el elemento del menu

ArchivoMenu.add_command(label="Nuevo")
ArchivoMenu.add_command(label="Abrir", command=abreAcrh)
ArchivoMenu.add_separator()
ArchivoMenu.add_command(label="Guardar")
ArchivoMenu.add_command(label="Guardar Como")
ArchivoMenu.add_separator()
ArchivoMenu.add_command(label="Cerrar", command=cerrarDoc)
ArchivoMenu.add_command(label="Salir", command=salirApp)

EdicionMenu=Menu(barraMenu, tearoff=0)

EdicionMenu.add_command(label="Copiar")
EdicionMenu.add_command(label="Cortar")
EdicionMenu.add_command(label="Pegar")

HerramientaMenu=Menu(barraMenu, tearoff=0)

HerramientaMenu.add_command(label="Reemplazar")

AyudaMenu=Menu(barraMenu, tearoff=0)

AyudaMenu.add_command(label="Licencia", command=infoLicencia)
AyudaMenu.add_command(label="Acerca de ...", command=infoAdicional)


# se crean los menus

barraMenu.add_cascade(label="Archivo", menu=ArchivoMenu)
barraMenu.add_cascade(label="Edicion", menu=EdicionMenu)
barraMenu.add_cascade(label="Herramientas", menu=HerramientaMenu)
barraMenu.add_cascade(label="Ayuda", menu=AyudaMenu)

# Se añaden los subelementos

raiz.mainloop()