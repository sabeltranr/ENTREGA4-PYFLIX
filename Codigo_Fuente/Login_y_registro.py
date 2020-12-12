import Info_WebScraping
from Info_WebScraping import obtencion_De_datos
import tkinter
from tkinter import *
from tkinter import messagebox
import PIL
from PIL import ImageTk, Image
from Pyflix import menu_programas

def aniadir_al_reg(usuario,contrasenia):
    """
    Recibe el nickname y la contraseña ingresada por el usuario en la sección de registro, realizando una verificación
    previa al guardado de dichos datos, esto para evitar crear de nuevo cuentas de usuarios ya registrados previamente,
    presentando en la interfaz mensaje de advertencia o éxito respectivamente.

    :param usuario:
    :param contrasenia:
    :return:
    """
    mi_diccionario = {}
    with open('Programas_Canales/usuarios.txt') as my_usuarios:
        usernames = my_usuarios.read()
        lista = usernames.split(',')
        for i in range(len(lista)):
            usuario_indi = lista[i].split('-')
            mi_diccionario[usuario_indi[0].strip()] = usuario_indi[1].strip()

    with open('Programas_Canales/usuarios.txt','a+') as my_usuarios:
        if usuario not in mi_diccionario.keys():
            my_usuarios.write(','+str(usuario)+'-'+str(contrasenia))
            registro_completo = messagebox.showinfo(message="Registro EXITOSO!!")

        else:
            aviso = messagebox.showwarning(title = "Usuario ya existente", message= "El usuario ya se encuentra registrado")
def comparacion_contra(contra1,contra2,usuario):
    """
    Recibe la contraseña base y la confirmación de la misma, esto para verificar que ambas son iguales y dar paso al
    registro del nuevo usuario en la base de datos; de caso contrario, aparece un mensaje de error

    :param contra1:
    :param contra2:
    :param usuario:
    :return:
    """
    if contra1 == contra2:
        aniadir_al_reg(usuario, contra1)
    else:
        nocoincide = messagebox.showerror(message="Las contraseñas no coinciden")

def login_grafica():
    """
    Función encargada de crear la interfaz gráfica del Login de inicio de sesión donde se encuentran los cuadros de
    entrada para el ingreso de datos, además de los botones de registro y acceso, los cuales llamaran las
    funciones correspondientes que realizan el proceso de verificación de datos.

    :return:
    """
    ventana = Tk()
    ventana.title ("Login")
    ventana.geometry("500x500")
    ventana.resizable(0,0)

    fondo = PhotoImage(file = "Imagenes/fondo_login.png")
    fondo_label = Label(ventana, image = fondo).place(x=0, y=0)

    nombredeusuario = tkinter.Entry(ventana, width = 38 )
    nombredeusuario.place(x=220, y = 179)
    password = tkinter.Entry(ventana,width = 38,show = '*')
    password.place(x = 220, y=267)



    fondo_botonres = Image.open('Imagenes/boton_Registro.png')
    fondo_botonres = fondo_botonres.resize((150, 150), Image.ANTIALIAS)
    fondo_botonres = ImageTk.PhotoImage(fondo_botonres)
    boton_registro = tkinter.Button(ventana, image=fondo_botonres,
                                    bg = 'brown3',width =150,height = 90,
                                    command = lambda: login_registro())
    boton_registro.place(x= 60, y = 350)

    fondo_botoning = Image.open('Imagenes/boton_inicio.png')
    fondo_botoning = fondo_botoning.resize((150, 150), Image.ANTIALIAS)
    fondo_botoning = ImageTk.PhotoImage(fondo_botoning)
    boton_getin = tkinter.Button(ventana,
                                 image=fondo_botoning,
                                 bg='violetred4',
                                 width=100,  height=90,
                                 command=lambda: login_inicio_sesion(nombredeusuario.get(), password.get(),ventana))
    boton_getin.place(x=320, y=350)
    ventana.mainloop()

def login_inicio_sesion(usuario,contra,ventana):
    """
    Recibe como parámetro de funcionamiento los datos ingresados en los Entry de la interfaz gráfica, y realiza
    3 verificaciones con estos:
     - Si recibe datos nulos o información vacía, informa por medio de un messagebox, de que los datos no son válidos.
     - Los datos ingresados son comparados con los existentes en la base de datos de usuarios, si el usuario ya se
        encuentra registrado, se verifica si la contraseña ingresada corresponde a la misma asignada al usuario, y a partir de
        allí se define si se permite el acceso o la contraseña esta incorrecta.
     - Si los datos ingresados después de ser comparados en la base de datos, no existen, se sugiere que el usuario se registre
     haciendo click en dicho botón correspondiente.

    :param usuario:
    :param contra:
    :param ventana:
    :return:
    """
    mi_diccionario = {}
    with open('Programas_Canales/usuarios.txt') as my_usuarios:
        usernames = my_usuarios.read()
        lista = usernames.split(',')
        for i in range(len(lista)):
            usuario_indi = lista[i].split('-')
            mi_diccionario[usuario_indi[0].strip()] = usuario_indi[1].strip()
        if usuario == '' and contra == '':
            empty = messagebox.showinfo(title = "Ingresa algun dato", message = 'No puedes dejar espacios en blanco')
        else:
            if usuario in mi_diccionario.keys():
                if contra == mi_diccionario[usuario]:
                    success = messagebox.showinfo(message='Bienvenid@ '+usuario+'!', title='Exito!!')
                    ventana.destroy()
                    menu_programas(usuario)

                else:
                    success = messagebox.showinfo(message="Contraseña incorrecta", title="Cuidado!")
            else:
                error = messagebox.showinfo(
                    message='No estas registrado,para hacerlo solo haz click en el boton de "Registrase" ' )

def login_registro():
    """
    Crea la ventana emergente de la sección grafica del registro de nuevo usuario, y a partir de los datos proporcionados
    en los espacios de entrada, los envía a la comparación y verificación de contraseñas para realizar el debido
    registro del nuevo usuario en la base de datos.

    :return:
    """
    registro = Toplevel()
    registro.title("Login")
    registro.geometry("300x400")
    registro.resizable(0, 0)
    fondo = PhotoImage(file="Imagenes/regis.png")
    fondo_registro = Label(registro, image=fondo).place(x=0, y=0)
    #Nombre de usuario
    nombre = tkinter.Entry(registro, width = 20 )
    nombre.place(x = 160, y = 119)
    #Apellido de usuario
    apellido = tkinter.Entry(registro, width=20)
    apellido.place(x=160, y=167)
    #Username
    usuario  = tkinter.Entry(registro, width=20)
    usuario.place(x=160, y=216)
    #Contraseña y confirmacion
    contra = tkinter.Entry(registro, width=20, show = '*')
    contra.place(x=160, y=268)
    confi_contra = tkinter.Entry(registro, width = 20, show = '*' )
    confi_contra.place(x = 160, y = 320)

    #Boton confirmacion
    Listo = Button(registro,
                   text= "Listo!",
                   bg = 'Gold',
                   command = lambda: comparacion_contra(contra.get(),confi_contra.get(),usuario.get()))
    Listo.place(x=130, y = 360)


    registro.mainloop()

def main_login():
    """
    Define el inicio del programa pues invoca al login y la biblioteca encargada del Web-Scrapping, será siempre la
    primera ventana en enseñarse cuando se ejecute el programa.
    :return:
    """
    obtencion_De_datos()
    login_grafica()
main_login()