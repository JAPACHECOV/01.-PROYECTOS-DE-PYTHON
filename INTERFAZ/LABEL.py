

from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=1000, height=800)
miFrame.pack ()

# LABEL tipo 1 con variable

# miLabel=Label(miFrame, text="Hola Mundo")
# miLabel.place(x=100,y=200)
# raiz.mainloop()


# LABEL tipo 2  compacta


# Label(miFrame, text="Hola Mundo", fg="Red", font=("Comic Sans MS",18)). place(x=100,y=200)
# raiz.mainloop()

# LABEL tipo 3  agregar Imagen

miImagen=PhotoImage(file= "paisaje.png")  # tiene que ser un .png
Label(miFrame, image=miImagen).place(x=0, y =0)
raiz.mainloop()

