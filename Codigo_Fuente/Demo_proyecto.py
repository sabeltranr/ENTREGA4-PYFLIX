import tkinter
import CanalBusca
from CanalBusca import *
from tkinter import PhotoImage
from tkinter import *
from PIL import Image,ImageTk

def ventana_infantil():
    """
    Crea una ventana emergente donde se estima que se muestre la programación diaria del canal infantil llamado PequeTv
    :return:None
    """
    raiz_infantil = Tk()
    raiz_infantil.title("PequeTv")
    raiz_infantil.resizable(0, 0)
    raiz_infantil.config(width=500,height=500,bg="white")
    raiz_infantil.mainloop()

def ventana_accion():
    """
    Crea una ventana emergente donde se estima que se muestre la programación diaria del canal acción llamado Boom Cinema
    :return:None
    """
    raiz_accion = Tk()
    raiz_accion.title("Boom Cinema")
    raiz_accion.resizable(0, 0)
    raiz_accion.config(width=500,height=500,bg="orange")
    raiz_accion.mainloop()

def ventana_terror():
    """
    Crea una ventana emergente donde se estima que se muestre la programación diaria del canal de terror llamado Deep Screams
    :return:None
    """
    raiz_terror = Tk()
    raiz_terror.title("Deep screams")
    raiz_terror.resizable(0, 0)
    raiz_terror.config(width=500,height=500,bg="black")
    raiz_terror.mainloop()

def ventana_comedia():
    """
    Crea una ventana emergente donde se estima que se muestre la programación diaria del canal de comedia llamado Tower of laughs
    :return:None
    """
    raiz_comedia = Tk()
    raiz_comedia.title("Tower of laughs")
    raiz_comedia.resizable(0, 0)
    raiz_comedia.config(width=500,height=500,bg="hotpink")
    raiz_comedia.mainloop()

def ventana_peliculas():
    """
    Crea una ventana emergente donde se estima que se muestre la programación diaria del canal de películas llamado Cara de Col
    :return:None
    """
    raiz_peliculas = Tk()
    raiz_peliculas.title("Cara de col")
    raiz_peliculas.resizable(0, 0)
    raiz_peliculas.config(width=500,height=500,bg="blue")
    raiz_peliculas.mainloop()
def main():
    """
    Funcion principal donde se ejecuta la ventana base donde se encuentran ubicados los botones que invocan ventanas
    emergentes
    :return: None
    """
    # Caracteristicas de ventana principal
    base = tkinter.Tk()
    base.geometry("1280x720")
    base.title('Buscador de Canales')
    base.config(bg='black')
    base.resizable(0,0)
    # Fondo de la ventana
    fondo = PhotoImage(file="Fondo.png")
    fondo2 = Label(base, image=fondo).place(x=0, y=0)

    # Barra de Busqueda
    barra_busqueda = tkinter.Entry(base, width=90)
    barra_busqueda.place(x=360, y=30)

    # Boton1 para invocar al canal 1
    fondo_boton1 = Image.open('Logo_CaradeCol.png')
    fondo_boton1 = fondo_boton1.resize((200, 150), Image.ANTIALIAS)  # Redimension (Alto, Ancho)
    fondo_boton1 = ImageTk.PhotoImage(fondo_boton1)
    boton1 = tkinter.Button(base, image=fondo_boton1,
                            text="Cara de Col",
                            compound="top", bg='Dodgerblue4',
                            fg='White',
                            font = ("Calibri",11),
                            command = lambda: ventana_peliculas())
    boton1.place(x=120, y=150)

    # Boton2 para invocar al canal 2
    fondo_boton2 = Image.open('Logo_PequeTv.png')
    fondo_boton2 = fondo_boton2.resize((200, 150), Image.ANTIALIAS)  # Redimension (Alto, Ancho)
    fondo_boton2 = ImageTk.PhotoImage(fondo_boton2)
    boton2 = tkinter.Button(base, image=fondo_boton2,
                            text="PequeTv",
                            compound="top",
                            bg='SeaGreen3',
                            fg='White',
                            font = ("Calibri",11),
                            command = lambda: ventana_infantil())
    boton2.place(x=540, y=150)

    # Boton3 para invocar al canal 3
    fondo_boton3 = Image.open('Logo_BoomCinema.png')
    fondo_boton3 = fondo_boton3.resize((200, 150), Image.ANTIALIAS)  # Redimension (Alto, Ancho)
    fondo_boton3 = ImageTk.PhotoImage(fondo_boton3)
    boton3 = tkinter.Button(base, image=fondo_boton3,
                            text="Boom Cinema",
                            compound="top",
                            bg='Burlywood1',
                            fg='black',
                            font = ("Calibri",11),
                            command = lambda: ventana_accion())
    boton3.place(x=960, y=150)

    # Boton3 para invocar al canal 4
    fondo_boton4 = Image.open('Logo_TowerofLaughs.png')
    fondo_boton4 = fondo_boton4.resize((200, 150), Image.ANTIALIAS)  # Redimension (Alto, Ancho)
    fondo_boton4 = ImageTk.PhotoImage(fondo_boton4)
    boton4 = tkinter.Button(base,
                            image=fondo_boton4,
                            text="Tower Of Laughs",
                            compound="top",
                            bg='white',
                            fg='black',
                            font = ("Calibri",11),
                            command = lambda : ventana_comedia())
    boton4.place(x=330, y=400)

    # Boton3 para invocar al canal 5
    fondo_boton5 = Image.open('Logo_DeepScreams.png')
    fondo_boton5 = fondo_boton5.resize((200, 150), Image.ANTIALIAS)  # Redimension (Alto, Ancho)
    fondo_boton5 = ImageTk.PhotoImage(fondo_boton5)
    boton5 = tkinter.Button(base,
                            image=fondo_boton5,
                            text="Deep Screams",
                            compound="top",
                            bg='Black',
                            fg='white',
                            font = ("Calibri",11),
                            command = lambda: ventana_terror())
    boton5.place(x=750, y=400)

    # Boton6 para busqueda
    # Boton6 para busqueda
    fondo_boton6 = Image.open('Lupita.jpg')
    fondo_boton6 = fondo_boton6.resize((15, 15), Image.ANTIALIAS)  # Redimension (Alto, Ancho)
    fondo_boton6 = ImageTk.PhotoImage(fondo_boton6)
    boton6 = tkinter.Button(base, image=fondo_boton6, bg='white', command=lambda: buscador(barra_busqueda.get()))
    boton6.place(x=900, y=30)

    base.mainloop()
main()


