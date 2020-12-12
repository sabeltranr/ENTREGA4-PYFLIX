import tkinter
from CanalBusca import *
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
contador = 0
def resultado_busqueda(resultado):
    try:
        nombre = resultado.split('\n')
        nombre_1 = nombre[2].split(':')
        nombre_2 = nombre_1[1].strip()
        raiz_resultado = Toplevel()
        raiz_resultado.title("Coincidencia de busqueda")
        raiz_resultado.resizable(0, 0)
        raiz_resultado.config(width=500, height=500, bg="white")
        #frame base
        my_frame = Frame(raiz_resultado)
        my_frame.pack()
        my_frame.config(width=500, height=500, bg="white", relief="groove", bd=30)

        #scroll y canva base
        barra = Scrollbar(my_frame, orient=VERTICAL)
        canva_resultado = Canvas(my_frame, bg='white', width=400, height=400, yscrollcommand=barra.set)

        frame_contenido = Frame(canva_resultado, bg='white')
        frame_contenido.place(x=0, y=0)

        canva_resultado.pack(side="left", fill="both", expand=True)
        canva_resultado.create_window(50, 30, window=frame_contenido, anchor="nw")
        barra.config(command=canva_resultado.yview)
        barra.pack(side=RIGHT, fill=Y)
        texto_Result = Label(frame_contenido,
                             wraplength=300,
                             text= resultado,
                             font=('Arial', 10),
                             background="White",
                             anchor = "nw",
                             justify = CENTER)
        texto_Result.pack()

        Imagen_result = Image.open("Imagenes/"+ nombre_2 +".png")
        Imagen_result = Imagen_result.resize((170, 240), Image.ANTIALIAS)  # Redimension (Alto, Ancho)
        Imagen_result = ImageTk.PhotoImage(Imagen_result)
        img_res_label = Label(frame_contenido, image=Imagen_result)
        img_res_label.pack()

        label_blanco1 = Label(frame_contenido, bg="White", width=15, height=3)
        label_blanco1.pack()

        raiz_resultado.update()
        canva_resultado.config(scrollregion=canva_resultado.bbox("all"))
        raiz_resultado.config(width=500, height=500, bg="white")
        raiz_resultado.mainloop()

    except IndexError:
        raiz_resultado = Toplevel()
        raiz_resultado.title("Coincidencia de busqueda")
        raiz_resultado.resizable(0, 0)
        raiz_resultado.config(width=500, height=500, bg="white")
        my_frame = Frame(raiz_resultado)
        my_frame.pack()
        my_frame.config(width=500, height=500, bg="white", relief="groove", bd=30)
        Imagen_result = Image.open("Imagenes/Error.png")
        Imagen_result = Imagen_result.resize((400, 400), Image.ANTIALIAS)  # Redimension (Alto, Ancho)
        Imagen_result = ImageTk.PhotoImage(Imagen_result)
        img_res_label = Label(my_frame, image=Imagen_result)
        img_res_label.pack()
        texto_Result = tkinter.Label(my_frame,
                                     text=resultado,
                                     fg='White',
                                     bg='DarkGoldenrod1',
                                     font=("Calibri", 12),
                                     wraplength=300)
        texto_Result.place(x=35, y=350)

        raiz_resultado.mainloop()

def ventana_infantil():
    """
    Crea una ventana emergente donde muestra la programación del día, asignada para
    el canal infantil llamado PequeTv, cada programa está acompañado de su imagen representativa para identificar
    el programa en cuestión.

    :return:
    """
    raiz_infantil = Toplevel()
    raiz_infantil.title("PequeTv")
    raiz_infantil.resizable(0, 0)
    frame_infantil = Frame(raiz_infantil)

    frame_infantil.pack()
    frame_infantil.config(width=500, height=500, bg="SeaGreen3", relief="groove", bd=30)

    barra = Scrollbar(frame_infantil, orient=VERTICAL)
    canva_infantil = Canvas(frame_infantil, bg='white', width=400, height=400, yscrollcommand=barra.set)

    frame_contenido = Frame(canva_infantil, bg='blue')
    frame_contenido.place(x=0, y=0)

    frame_imagenes = Frame(canva_infantil, bg='white')
    frame_imagenes.place(x=200, y=0)
    canva_infantil.pack(side="left", fill="both", expand=True)
    canva_infantil.create_window(0, 0, window=frame_contenido, anchor="nw")
    canva_infantil.create_window(370, 10, window=frame_imagenes, anchor='ne')
    barra.config(command=canva_infantil.yview)
    barra.pack(side=RIGHT, fill=Y)
    with open("Programas_Canales/canal_infantil.txt", 'r') as progra_infantil:
        programacion = progra_infantil.read()
        programacion = programacion.split('|')
    cadena = ''
    for i in programacion:
        cadena += i + '\n' + '-------------------------------------------------' + '\n'
    texto = Label(frame_contenido,
                  wraplength=200,
                  text=cadena,
                  font=('Arial', 10),
                  background="White",
                  anchor="nw",
                  justify=LEFT)
    dic_infantil = {1: "Imagenes/Doctora Juguetes.png", 2: "Imagenes/Efelante.png", 3: "Imagenes/Gigantosaurus.png",
                    4: "Imagenes/Aventuras en Paniales.png", 5: "Imagenes/Pinky Dinky doo.png",
                    6: "Imagenes/CatDog.png", 7: "Imagenes/Narigota.png", 8: "Imagenes/Rolie Polie Olie.png",
                    9: "Imagenes/Clifford,el gran perro rojo.png", 10: "Imagenes/Dinosaurio.png"}

    doctora = Image.open(dic_infantil[1])
    doctora = doctora.resize((120, 170), Image.ANTIALIAS)
    doctora = ImageTk.PhotoImage(doctora)
    doctora_label = Label(frame_imagenes, image= doctora)
    doctora_label.pack()

    label_blanco1 = Label(frame_imagenes, bg="White", width=15, height=3)
    label_blanco1.pack()

    efelante = Image.open(dic_infantil[2])
    efelante = efelante.resize((120, 170), Image.ANTIALIAS)
    efelante = ImageTk.PhotoImage(efelante)
    efelante_label = Label(frame_imagenes, image=efelante)
    efelante_label.pack()

    label_blanco2 = Label(frame_imagenes, bg="White", width=15, height=4)
    label_blanco2.pack()

    gigantosaurus = Image.open(dic_infantil[3])
    gigantosaurus = gigantosaurus.resize((120, 170), Image.ANTIALIAS)
    gigantosaurus = ImageTk.PhotoImage(gigantosaurus)
    gigantosaurus_label = Label(frame_imagenes, image=gigantosaurus)
    gigantosaurus_label.pack()

    label_blanco3 = Label(frame_imagenes, bg="White", width=15, height=4)
    label_blanco3.pack()

    rugrats = Image.open(dic_infantil[4])
    rugrats = rugrats.resize((120, 170), Image.ANTIALIAS)
    rugrats = ImageTk.PhotoImage(rugrats)
    rugrats_label = Label(frame_imagenes, image=rugrats)
    rugrats_label.pack()

    label_blanco4 = Label(frame_imagenes, bg="White", width=15, height=4)
    label_blanco4.pack()

    pinky = Image.open(dic_infantil[5])
    pinky = pinky.resize((120, 170), Image.ANTIALIAS)
    pinky = ImageTk.PhotoImage(pinky)
    pinky_label = Label(frame_imagenes, image=pinky)
    pinky_label.pack()

    label_blanco5 = Label(frame_imagenes, bg="White", width=15, height=4)
    label_blanco5.pack()

    catdog = Image.open(dic_infantil[6])
    catdog = catdog.resize((120, 170), Image.ANTIALIAS)
    catdog = ImageTk.PhotoImage(catdog)
    catdog_label = Label(frame_imagenes, image=catdog)
    catdog_label.pack()

    label_blanco6 = Label(frame_imagenes, bg="White", width=15, height=4)
    label_blanco6.pack()

    narigota = Image.open(dic_infantil[7])
    narigota = narigota.resize((120, 170), Image.ANTIALIAS)
    narigota = ImageTk.PhotoImage(narigota)
    narigota_label = Label(frame_imagenes, image=narigota)
    narigota_label.pack()

    label_blanco7 = Label(frame_imagenes, bg="White", width=15, height=4)
    label_blanco7.pack()

    rolie = Image.open(dic_infantil[8])
    rolie = rolie.resize((120, 170), Image.ANTIALIAS)
    rolie = ImageTk.PhotoImage(rolie)
    rolie_label = Label(frame_imagenes, image=rolie)
    rolie_label.pack()

    label_blanco8 = Label(frame_imagenes, bg="White", width=15, height=3)
    label_blanco8.pack()

    clifford = Image.open(dic_infantil[9])
    clifford = clifford.resize((120, 170), Image.ANTIALIAS)
    clifford = ImageTk.PhotoImage(clifford)
    clifford_label = Label(frame_imagenes, image=clifford)
    clifford_label.pack()

    label_blanco9 = Label(frame_imagenes, bg="White", width=15, height=2)
    label_blanco9.pack()

    dinosaurio = Image.open(dic_infantil[10])
    dinosaurio = dinosaurio.resize((120, 170), Image.ANTIALIAS)
    dinosaurio = ImageTk.PhotoImage(dinosaurio)
    dinosaurio_label = Label(frame_imagenes, image=dinosaurio)
    dinosaurio_label.pack()

    texto.pack()
    raiz_infantil.update()
    canva_infantil.config(scrollregion=canva_infantil.bbox("all"))
    raiz_infantil.config(width=500,height=500,bg="white")
    raiz_infantil.mainloop()

def ventana_accion():
    """
    Crea una ventana emergente donde muestra la programación del día, asignada para
    el canal acción llamado Boom Cinema, cada programa está acompañado de su imagen representativa para identificar
    el programa en cuestión.


    :return:
    """
    raiz_accion = Toplevel()
    raiz_accion.title("Boom Cinema")
    raiz_accion.resizable(0, 0)

    frame_accion = Frame(raiz_accion)
    frame_accion.pack()
    frame_accion.config(width=500, height=500, bg="chocolate2", relief="groove", bd=30)

    barra = Scrollbar(frame_accion, orient=VERTICAL)
    canva_accion = Canvas(frame_accion, bg='white', width=400, height=400, yscrollcommand=barra.set)

    frame_contenido = Frame(canva_accion, bg='blue')
    frame_contenido.place(x=0, y=0)

    frame_imagenes = Frame(canva_accion, bg='white')
    frame_imagenes.place(x=200, y=0)
    canva_accion.pack(side="left", fill="both", expand=True)
    canva_accion.create_window(0, 0, window=frame_contenido, anchor="nw")
    canva_accion.create_window(370, 30, window=frame_imagenes, anchor='ne')
    barra.config(command=canva_accion.yview)
    barra.pack(side=RIGHT, fill=Y)
    with open("Programas_Canales/canal_accion.txt", 'r') as progra_accion:
        programacion = progra_accion.read()
        programacion = programacion.split('|')
    cadena = ''
    for i in programacion:
        cadena += i + '\n' + '-------------------------------------------------' + '\n'
    texto = Label(frame_contenido,
                  wraplength=200,
                  text=cadena,
                  font=('Arial', 10),
                  background="White",
                  anchor="nw",
                  justify=LEFT)
    dic_accion = {1: "Imagenes/Maze Runner.png", 2: "Imagenes/Vikingos.png", 3: "Imagenes/Escuadron 6.png",
                    4: "Imagenes/Arrow.png", 5: "Imagenes/Rambo.png", 6: "Imagenes/The Flash.png",
                    7: "Imagenes/Plan escape.png", 8: "Imagenes/La Vieja Guardia.png",
                    9: "Imagenes/3%.png", 10: "Imagenes/Terminator.png"}

    maze = Image.open(dic_accion[1])
    maze = maze.resize((120, 170), Image.ANTIALIAS)
    maze = ImageTk.PhotoImage(maze)
    maze_label = Label(frame_imagenes, image=maze)
    maze_label.pack()

    label_blanco1 = Label(frame_imagenes, bg="White", width=15, height=3)
    label_blanco1.pack()

    vikingos = Image.open(dic_accion[2])
    vikingos = vikingos.resize((120, 170), Image.ANTIALIAS)
    vikingos = ImageTk.PhotoImage(vikingos)
    vikingos_label = Label(frame_imagenes, image=vikingos)
    vikingos_label.pack()

    label_blanco2 = Label(frame_imagenes, bg="White", width=15, height=3)
    label_blanco2.pack()

    escuadron = Image.open(dic_accion[3])
    escuadron = escuadron.resize((120, 170), Image.ANTIALIAS)
    escuadron = ImageTk.PhotoImage(escuadron)
    escuadron_label = Label(frame_imagenes, image=escuadron)
    escuadron_label.pack()

    label_blanco3 = Label(frame_imagenes, bg="White", width=15, height=3)
    label_blanco3.pack()

    arrow = Image.open(dic_accion[4])
    arrow = arrow.resize((120, 170), Image.ANTIALIAS)
    arrow = ImageTk.PhotoImage(arrow)
    arrow_label = Label(frame_imagenes, image=arrow)
    arrow_label.pack()

    label_blanco4 = Label(frame_imagenes, bg="White", width=15, height=3)
    label_blanco4.pack()

    rambo = Image.open(dic_accion[5])
    rambo = rambo.resize((120, 170), Image.ANTIALIAS)
    rambo = ImageTk.PhotoImage(rambo)
    rambo_label = Label(frame_imagenes, image=rambo)
    rambo_label.pack()

    label_blanco5 = Label(frame_imagenes, bg="White", width=15, height=3)
    label_blanco5.pack()

    flash = Image.open(dic_accion[6])
    flash = flash.resize((120, 170), Image.ANTIALIAS)
    flash = ImageTk.PhotoImage(flash)
    flash_label = Label(frame_imagenes, image=flash)
    flash_label.pack()

    label_blanco6 = Label(frame_imagenes, bg="White", width=15, height=3)
    label_blanco6.pack()

    escape = Image.open(dic_accion[7])
    escape = escape.resize((120, 170), Image.ANTIALIAS)
    escape = ImageTk.PhotoImage(escape)
    escape_label = Label(frame_imagenes, image=escape)
    escape_label.pack()

    label_blanco7 = Label(frame_imagenes, bg="White", width=15, height=3)
    label_blanco7.pack()

    vieja_guardia = Image.open(dic_accion[8])
    vieja_guardia = vieja_guardia.resize((120, 170), Image.ANTIALIAS)
    vieja_guardia = ImageTk.PhotoImage(vieja_guardia)
    vieja_guardia_label = Label(frame_imagenes, image=vieja_guardia)
    vieja_guardia_label.pack()

    label_blanco8 = Label(frame_imagenes, bg="White", width=15, height=3)
    label_blanco8.pack()

    tresporciento = Image.open(dic_accion[9])
    tresporciento = tresporciento.resize((120, 170), Image.ANTIALIAS)
    tresporciento = ImageTk.PhotoImage(tresporciento)
    tresporciento_label = Label(frame_imagenes, image=tresporciento)
    tresporciento_label.pack()

    label_blanco9 = Label(frame_imagenes, bg="White", width=15, height=3)
    label_blanco9.pack()

    terminator = Image.open(dic_accion[10])
    terminator = terminator.resize((120, 170), Image.ANTIALIAS)
    terminator = ImageTk.PhotoImage(terminator)
    terminator_label = Label(frame_imagenes, image=terminator)
    terminator_label.pack()

    texto.pack()
    raiz_accion.update()
    canva_accion.config(scrollregion=canva_accion.bbox("all"))
    raiz_accion.config(width=500,height=500,bg="orange")
    raiz_accion.mainloop()

def ventana_terror():
    """
    Crea una ventana emergente donde muestra la programación del día, asignada para el
    canal de terror llamado Deep Screams, cada programa está acompañado de su imagen representativa para identificar
    el programa en cuestión.

    :return:
    """
    raiz_terror = Toplevel()
    raiz_terror.title("Deep screams")
    raiz_terror.resizable(0, 0)

    frame_terror = Frame(raiz_terror)
    frame_terror.pack()
    frame_terror.config(width=500, height=500, bg="gray4", relief="groove", bd=30)

    barra = Scrollbar(frame_terror, orient=VERTICAL)
    canva_terror = Canvas(frame_terror, bg='black', width=400, height=400, yscrollcommand=barra.set)

    frame_contenido = Frame(canva_terror, bg='black')
    frame_contenido.place(x=0, y=0)

    frame_imagenes = Frame(canva_terror, bg='black')
    frame_imagenes.place(x=200, y=0)
    canva_terror.pack(side="left", fill="both", expand=True)
    canva_terror.create_window(0, 0, window=frame_contenido, anchor="nw")
    canva_terror.create_window(370, 20, window=frame_imagenes, anchor='ne')
    barra.config(command=canva_terror.yview)
    barra.pack(side=RIGHT, fill=Y)
    with open("Programas_Canales/canal_terror.txt", 'r') as progra_peli:
        programacion = progra_peli.read()
        programacion = programacion.split('|')
    cadena = ''
    for i in programacion:
        cadena += i + '\n' + '-------------------------------------------------' + '\n'
    texto = Label(frame_contenido,
                  wraplength=200,
                  text=cadena,
                  font=('Arial', 10),
                  fg = "white",
                  background="black",
                  anchor="nw",
                  justify=LEFT)
    dic_terror = {1: "Imagenes/Shutter.png", 2: "Imagenes/El Exorcista.png", 3: "Imagenes/Marianne.png",
                  4: "Imagenes/Veronica.png", 5: "Imagenes/La Morgue.png", 6: "Imagenes/Creepypasta.png",
                  7: "Imagenes/Insidious 3.png", 8: "Imagenes/El Aro.png", 9: "Imagenes/La Maldicion.png",
                  10: "Imagenes/Halloween.png", 11: "Imagenes/Mama.png", 12: "Imagenes/Siniestro.jpg"}

    shutter = Image.open(dic_terror[1])
    shutter = shutter.resize((120, 170), Image.ANTIALIAS)
    shutter = ImageTk.PhotoImage(shutter)
    shutter_label = Label(frame_imagenes, image= shutter)
    shutter_label.pack()

    label_negro1 = Label(frame_imagenes, bg="black", width=15, height=3)
    label_negro1.pack()

    exorcista = Image.open(dic_terror[2])
    exorcista = exorcista.resize((120, 170), Image.ANTIALIAS)
    exorcista = ImageTk.PhotoImage(exorcista)
    exorcista_label = Label(frame_imagenes, image=exorcista)
    exorcista_label.pack()

    label_negro2 = Label(frame_imagenes, bg="black", width=15, height=4)
    label_negro2.pack()

    marianne = Image.open(dic_terror[3])
    marianne = marianne.resize((120, 170), Image.ANTIALIAS)
    marianne = ImageTk.PhotoImage(marianne)
    marianne_label = Label(frame_imagenes, image=marianne)
    marianne_label.pack()

    label_negro3 = Label(frame_imagenes, bg="black", width=15, height=3)
    label_negro3.pack()

    veronica = Image.open(dic_terror[4])
    veronica = veronica.resize((120, 170), Image.ANTIALIAS)
    veronica = ImageTk.PhotoImage(veronica)
    veronica_label = Label(frame_imagenes, image=veronica)
    veronica_label.pack()

    label_negro4 = Label(frame_imagenes, bg="black", width=15, height=5)
    label_negro4.pack()

    morgue = Image.open(dic_terror[5])
    morgue = morgue.resize((120, 170), Image.ANTIALIAS)
    morgue = ImageTk.PhotoImage(morgue)
    morgue_label = Label(frame_imagenes, image=morgue)
    morgue_label.pack()

    label_negro5 = Label(frame_imagenes, bg="black", width=15, height=4)
    label_negro5.pack()

    creepy = Image.open(dic_terror[6])
    creepy = creepy.resize((120, 170), Image.ANTIALIAS)
    creepy = ImageTk.PhotoImage(creepy)
    creepy_label = Label(frame_imagenes, image=creepy)
    creepy_label.pack()

    label_negro6 = Label(frame_imagenes, bg="black", width=15, height=3)
    label_negro6.pack()

    insidious = Image.open(dic_terror[7])
    insidious = insidious.resize((120, 170), Image.ANTIALIAS)
    insidious = ImageTk.PhotoImage(insidious)
    insidious_label = Label(frame_imagenes, image=insidious)
    insidious_label.pack()

    label_negro7 = Label(frame_imagenes, bg="black", width=15, height=3)
    label_negro7.pack()

    aro = Image.open(dic_terror[8])
    aro = aro.resize((120, 170), Image.ANTIALIAS)
    aro = ImageTk.PhotoImage(aro)
    aro_label = Label(frame_imagenes, image=aro)
    aro_label.pack()

    label_negro8 = Label(frame_imagenes, bg="black", width=15, height=3)
    label_negro8.pack()

    maldicion = Image.open(dic_terror[9])
    maldicion = maldicion.resize((120, 170), Image.ANTIALIAS)
    maldicion = ImageTk.PhotoImage(maldicion)
    maldicion_label = Label(frame_imagenes, image=maldicion)
    maldicion_label.pack()

    label_negro9 = Label(frame_imagenes, bg="black", width=15, height=2)
    label_negro9.pack()

    halloween = Image.open(dic_terror[10])
    halloween = halloween.resize((120, 170), Image.ANTIALIAS)
    halloween = ImageTk.PhotoImage(halloween)
    halloween_label = Label(frame_imagenes, image=halloween)
    halloween_label.pack()

    label_negro10 = Label(frame_imagenes, bg="black", width=15, height=4)
    label_negro10.pack()

    mama = Image.open(dic_terror[11])
    mama = mama.resize((120, 170), Image.ANTIALIAS)
    mama = ImageTk.PhotoImage(mama)
    mama_label = Label(frame_imagenes, image=mama)
    mama_label.pack()

    label_negro11 = Label(frame_imagenes, bg="black", width=15, height=3)
    label_negro11.pack()

    siniestro = Image.open(dic_terror[12])
    siniestro = siniestro.resize((120, 170), Image.ANTIALIAS)
    siniestro = ImageTk.PhotoImage(siniestro)
    siniestro_label = Label(frame_imagenes, image=siniestro)
    siniestro_label.pack()

    texto.pack()
    raiz_terror.update()
    canva_terror.config(scrollregion=canva_terror.bbox("all"))
    raiz_terror.config(width=500,height=500,bg="black")
    raiz_terror.mainloop()

def ventana_comedia():
    """
    Crea una ventana emergente donde muestra la programación del día, asignada para el
    canal de comedia llamado Tower of laughs, cada programa está acompañado de su imagen representativa para identificar
    el programa en cuestión.

    :return:
    """
    raiz_comedia = Toplevel()
    raiz_comedia.title("Tower of laughs")
    raiz_comedia.resizable(0, 0)

    frame_comedia = Frame(raiz_comedia)
    frame_comedia.pack()
    frame_comedia.config(width=500, height=500, bg="brown1", relief="groove", bd=30)

    barra = Scrollbar(frame_comedia, orient=VERTICAL)
    canva_comedia = Canvas(frame_comedia, bg='white', width=400, height=400, yscrollcommand=barra.set)

    frame_contenido = Frame(canva_comedia, bg='blue')
    frame_contenido.place(x=0, y=0)

    frame_imagenes = Frame(canva_comedia, bg='white')
    frame_imagenes.place(x=200, y=0)
    canva_comedia.pack(side="left", fill="both", expand=True)
    canva_comedia.create_window(0, 0, window=frame_contenido, anchor="nw")
    canva_comedia.create_window(370, 20, window=frame_imagenes, anchor='ne')
    barra.config(command=canva_comedia.yview)
    barra.pack(side=RIGHT, fill=Y)
    with open("Programas_Canales/canal_comedia.txt", 'r') as progra_peli:
        programacion = progra_peli.read()
        programacion = programacion.split('|')
    cadena = ''
    for i in programacion:
        cadena += i + '\n' + '-------------------------------------------------' + '\n'
    texto = Label(frame_contenido,
                  wraplength=200,
                  text=cadena,
                  font=('Arial', 10),
                  background="White",
                  anchor="nw",
                  justify=LEFT)
    dic_comedia = {1: "Imagenes/El lobo de Wall street.png", 2: "Imagenes/Sandy Wexler.png",
                   3: "Imagenes/La otra Missy.png", 4: "Imagenes/The Sleepover.png",
                   5: "Imagenes/Grandes espias.png", 6: "Imagenes/Misterio a bordo.png", 7: "Imagenes/Duff.png",
                   8: "Imagenes/El gran dictador.png", 9: "Imagenes/Miss Simpatia.png", 10: "Imagenes/Friends.png",
                   11: "Imagenes/Mi pobre angelito.png", 12:"Imagenes/La Familia P.Luche.png",
                   13:"Imagenes/La que se avecina.png"}

    lobo = Image.open(dic_comedia[1])
    lobo = lobo.resize((120, 170), Image.ANTIALIAS)
    lobo = ImageTk.PhotoImage(lobo)
    lobo_label = Label(frame_imagenes, image=lobo)
    lobo_label.pack()

    label_blanco1 = Label(frame_imagenes, bg="White", width=15, height=3)
    label_blanco1.pack()

    sandy = Image.open(dic_comedia[2])
    sandy = sandy.resize((120, 170), Image.ANTIALIAS)
    sandy = ImageTk.PhotoImage(sandy)
    sandy_label = Label(frame_imagenes, image=sandy)
    sandy_label.pack()

    label_blanco2 = Label(frame_imagenes, bg="White", width=15, height=2)
    label_blanco2.pack()

    missy = Image.open(dic_comedia[3])
    missy = missy.resize((120, 170), Image.ANTIALIAS)
    missy = ImageTk.PhotoImage(missy)
    missy_label = Label(frame_imagenes, image=missy)
    missy_label.pack()

    label_blanco3 = Label(frame_imagenes, bg="White", width=15, height=3)
    label_blanco3.pack()

    sleepover = Image.open(dic_comedia[4])
    sleepover = sleepover.resize((120, 170), Image.ANTIALIAS)
    sleepover = ImageTk.PhotoImage(sleepover)
    sleepover_label = Label(frame_imagenes, image=sleepover)
    sleepover_label.pack()

    label_blanco4 = Label(frame_imagenes, bg="White", width=15, height=3)
    label_blanco4.pack()

    espias = Image.open(dic_comedia[5])
    espias = espias.resize((120, 170), Image.ANTIALIAS)
    espias = ImageTk.PhotoImage(espias)
    espias_label = Label(frame_imagenes, image=espias)
    espias_label.pack()

    label_blanco5 = Label(frame_imagenes, bg="White", width=15, height=3)
    label_blanco5.pack()

    misterio = Image.open(dic_comedia[6])
    misterio = misterio.resize((120, 170), Image.ANTIALIAS)
    misterio = ImageTk.PhotoImage(misterio)
    misterio_label = Label(frame_imagenes, image=misterio)
    misterio_label.pack()

    label_blanco6 = Label(frame_imagenes, bg="White", width=15, height=3)
    label_blanco6.pack()

    duff = Image.open(dic_comedia[7])
    duff = duff.resize((120, 170), Image.ANTIALIAS)
    duff = ImageTk.PhotoImage(duff)
    duff_label = Label(frame_imagenes, image=duff)
    duff_label.pack()

    label_blanco7 = Label(frame_imagenes, bg="White", width=15, height=2)
    label_blanco7.pack()

    dictador = Image.open(dic_comedia[8])
    dictador = dictador.resize((120, 170), Image.ANTIALIAS)
    dictador = ImageTk.PhotoImage(dictador)
    dictador_label = Label(frame_imagenes, image=dictador)
    dictador_label.pack()

    label_blanco8 = Label(frame_imagenes, bg="White", width=15, height=2)
    label_blanco8.pack()

    miss_simpatia = Image.open(dic_comedia[9])
    miss_simpatia = miss_simpatia.resize((120, 170), Image.ANTIALIAS)
    miss_simpatia = ImageTk.PhotoImage(miss_simpatia)
    miss_simpatia_label = Label(frame_imagenes, image=miss_simpatia)
    miss_simpatia_label.pack()

    label_blanco9 = Label(frame_imagenes, bg="White", width=15, height=2)
    label_blanco9.pack()

    friends = Image.open(dic_comedia[10])
    friends = friends.resize((120, 170), Image.ANTIALIAS)
    friends = ImageTk.PhotoImage(friends)
    friends_label = Label(frame_imagenes, image=friends)
    friends_label.pack()

    label_blanco10 = Label(frame_imagenes, bg="White", width=15, height=2)
    label_blanco10.pack()

    angelito = Image.open(dic_comedia[11])
    angelito = angelito.resize((120, 170), Image.ANTIALIAS)
    angelito = ImageTk.PhotoImage(angelito)
    angelito_label = Label(frame_imagenes, image=angelito)
    angelito_label.pack()

    label_blanco10 = Label(frame_imagenes, bg="White", width=15, height=2)
    label_blanco10.pack()

    peluche = Image.open(dic_comedia[12])
    peluche = peluche.resize((120, 170), Image.ANTIALIAS)
    peluche = ImageTk.PhotoImage(peluche)
    peluche_label = Label(frame_imagenes, image=peluche)
    peluche_label.pack()

    label_blanco11 = Label(frame_imagenes, bg="White", width=15, height=3)
    label_blanco11.pack()

    avecina = Image.open(dic_comedia[13])
    avecina = avecina.resize((120, 170), Image.ANTIALIAS)
    avecina = ImageTk.PhotoImage(avecina)
    avecina_label = Label(frame_imagenes, image=avecina)
    avecina_label.pack()

    texto.pack()
    raiz_comedia.update()
    canva_comedia.config(scrollregion=canva_comedia.bbox("all"))
    raiz_comedia.config(width=500,height=500,bg="hotpink")
    raiz_comedia.mainloop()

def ventana_peliculas():
    """
    Crea una ventana emergente donde muestra la programación del día, asignada para el
    canal de películas llamado Cara de Col, cada programa está acompañado de su imagen representativa para identificar
    el programa en cuestión.

    :return:
    """
    raiz_peliculas = Toplevel()
    raiz_peliculas.title("Cara de col")
    raiz_peliculas.resizable(0, 0)

    frame_peliculas = Frame(raiz_peliculas)
    #frame para el borde
    frame_peliculas.pack()
    frame_peliculas.config(width=500, height=500, bg="blue", relief="groove", bd=30)
    #canva scroleable
    barra = Scrollbar(frame_peliculas, orient=VERTICAL)
    canva_pelicula = Canvas(frame_peliculas,bg = 'white',width=400,height= 400,yscrollcommand=barra.set)

    frame_contenido = Frame(canva_pelicula,bg = 'blue')
    frame_contenido.place(x = 0, y = 0)

    frame_imagenes = Frame(canva_pelicula, bg = 'white')
    frame_imagenes.place(x=200,y=0)
    canva_pelicula.pack(side="left",fill="both",expand= True)
    canva_pelicula.create_window(0, 0, window=frame_contenido, anchor="nw")
    canva_pelicula.create_window(370,10, window = frame_imagenes, anchor = 'ne')
    barra.config(command=canva_pelicula.yview)
    barra.pack(side=RIGHT, fill=Y)
    canal  = 'canal_peli'
    with open("Programas_Canales/"+canal+".txt", 'r') as progra_peli:
        programacion = progra_peli.read()
        programacion = programacion.split('|')
    cadena = ''
    for i in programacion:
        cadena += i + '\n'+'-------------------------------------------------'+'\n'
    texto = Label(frame_contenido,
                wraplength=200,
                text=cadena,
                font = ('Arial',10),
                background="White",
                anchor = "nw",
                justify = LEFT)
    diccionario_de_pelis = {1:"Imagenes/Spider-Man de regreso a casa.png",2:"Imagenes/Los Simpson La pelicula.png"
                            ,3:"Imagenes/Los Vengadores Infinity War.png",4:"Imagenes/Harry Potter y la camara secreta.png",
                            5:"Imagenes/Harry Potter y la Orden del Fenix.png",6:"Imagenes/Juego de armas.png",
                            7:"Imagenes/El destino de Jupiter.png",8:"Imagenes/Persecucion mortal.png",9:"Imagenes/Jack y jill.png",
                            10:"Imagenes/Frente al mar.png"}


    Spiderman = Image.open(diccionario_de_pelis[1])
    Spiderman = Spiderman.resize((120, 170), Image.ANTIALIAS)
    Spiderman = ImageTk.PhotoImage(Spiderman)
    spiderman_label = Label(frame_imagenes, image=Spiderman)
    spiderman_label.pack()

    label_blanco1 = Label(frame_imagenes, bg="White", width=15, height=1)
    label_blanco1.pack()

    simpson = Image.open(diccionario_de_pelis[2])
    simpson = simpson.resize((120, 170), Image.ANTIALIAS)
    simpson = ImageTk.PhotoImage(simpson)
    simpson_label = Label(frame_imagenes, image=simpson)
    simpson_label.pack()

    label_blanco2 = Label(frame_imagenes, bg="White", width=15, height=1)
    label_blanco2.pack()

    vengadores = Image.open(diccionario_de_pelis[3])
    vengadores = vengadores.resize((120, 170), Image.ANTIALIAS)
    vengadores = ImageTk.PhotoImage(vengadores)
    vengadores_label = Label(frame_imagenes, image=vengadores)
    vengadores_label.pack()

    label_blanco3 = Label(frame_imagenes,bg = "White",width = 15, height = 1)
    label_blanco3.pack()

    harry_Camara = Image.open(diccionario_de_pelis[4])
    harry_Camara = harry_Camara.resize((120, 170), Image.ANTIALIAS)
    harry_Camara = ImageTk.PhotoImage(harry_Camara)
    harry_Camara_label = Label(frame_imagenes, image=harry_Camara)
    harry_Camara_label.pack()

    label_blanco4 = Label(frame_imagenes, bg="White", width=15, height=1)
    label_blanco4.pack()

    harry_fenix = Image.open(diccionario_de_pelis[5])
    harry_fenix = harry_fenix.resize((120, 170), Image.ANTIALIAS)
    harry_fenix = ImageTk.PhotoImage(harry_fenix)
    harry_fenix_label = Label(frame_imagenes, image=harry_fenix)
    harry_fenix_label.pack()

    label_blanco5 = Label(frame_imagenes, bg="White", width=15, height=2)
    label_blanco5.pack()

    juego_armas = Image.open(diccionario_de_pelis[6])
    juego_armas = juego_armas.resize((120, 170), Image.ANTIALIAS)
    juego_armas = ImageTk.PhotoImage(juego_armas)
    juego_armas_label = Label(frame_imagenes, image=juego_armas)
    juego_armas_label.pack()

    label_blanco6 = Label(frame_imagenes, bg="White", width=15, height=2)
    label_blanco6.pack()

    jupiter = Image.open(diccionario_de_pelis[7])
    jupiter = jupiter.resize((120, 170), Image.ANTIALIAS)
    jupiter = ImageTk.PhotoImage(jupiter)
    jupiter_label = Label(frame_imagenes, image=jupiter)
    jupiter_label.pack()

    label_blanco7= Label(frame_imagenes, bg="White", width=15, height=2)
    label_blanco7.pack()

    persecucion = Image.open(diccionario_de_pelis[8])
    persecucion = persecucion.resize((120, 170), Image.ANTIALIAS)
    persecucion = ImageTk.PhotoImage(persecucion)
    persecucion_label = Label(frame_imagenes, image=persecucion)
    persecucion_label.pack()

    label_blanco8 = Label(frame_imagenes, bg="White", width=15, height=2)
    label_blanco8.pack()

    jack_jill = Image.open(diccionario_de_pelis[9])
    jack_jill = jack_jill.resize((120, 170), Image.ANTIALIAS)
    jack_jill = ImageTk.PhotoImage(jack_jill)
    jack_jill_label = Label(frame_imagenes, image=jack_jill)
    jack_jill_label.pack()

    label_blanco9 = Label(frame_imagenes, bg="White", width=15, height=2)
    label_blanco9.pack()

    frente_mar = Image.open(diccionario_de_pelis[10])
    frente_mar = frente_mar.resize((120, 170), Image.ANTIALIAS)
    frente_mar = ImageTk.PhotoImage(frente_mar)
    frente_mar_label = Label(frame_imagenes, image=frente_mar)
    frente_mar_label.pack()


    texto.pack()
    raiz_peliculas.update()
    canva_pelicula.config(scrollregion=canva_pelicula.bbox("all"))
    raiz_peliculas.config(width=500,height=500,bg="white")
    raiz_peliculas.mainloop()

def ventana_WebScrapping():

    """
    Crea una ventana emergente donde se muestran los datos obtenidos tras la realización del web scraping,
    al igual que el headlabel de la página, para hacer una recreación más fiel de la misma, en la plataforma creada.

    :return:
    """

    raiz_web = Toplevel()
    raiz_web.title("Proximos Estrenos")
    raiz_web.resizable(0, 0)

    frame_web = Frame(raiz_web)
    # frame para el borde
    frame_web.pack()
    frame_web.config(width=500, height=500, bg="purple", relief="groove", bd=30)
    # canva scroleable
    barra = Scrollbar(frame_web, orient=VERTICAL)
    canva_web = Canvas(frame_web, bg='white', width=400, height=400, yscrollcommand=barra.set)

    frame_contenido = Frame(canva_web, bg='white')
    frame_contenido.place(x=0, y=0)

    canva_web.pack(side="left", fill="both", expand=True)
    canva_web.create_window(0, 0, window=frame_contenido, anchor="nw")
    barra.config(command=canva_web.yview)
    barra.pack(side=RIGHT, fill=Y)

    Top_web = Image.open("Las 49 películas más esperadas de 2021.png")
    Top_web = Top_web.resize((450, 200), Image.ANTIALIAS)
    Top_web = ImageTk.PhotoImage(Top_web)
    Top_web_label = Label(frame_contenido, image=Top_web)
    Top_web_label.pack(side=TOP)

    with open("web.txt") as estrenos:
        estren_peli = estrenos.read()
        estren_peli = estren_peli.split('\n')
    cadena = ''
    for i in estren_peli:
        cadena += i + '\n' + '----------------------------------------------------------------------------------' + '\n'
    texto = Label(frame_contenido,
                  wraplength=400,
                  text=cadena,
                  font=('Arial', 10),
                  background="White",
                  anchor="nw",
                  justify=LEFT)
    texto.pack(side = LEFT)
    raiz_web.update()
    canva_web.config(scrollregion=canva_web.bbox("all"))
    raiz_web.config(width=500, height=500, bg="white")
    raiz_web.mainloop()

def ventana_historial(usuario):
    """
    Crea una ventana emergente donde se muestra el historial del usuario en sesión, recurriendo al llamado del
    archivo.txt donde se almacena esta información
    :param usuario:
    :return:
    """

    base_historial = Toplevel()
    base_historial.title("Tu Historial de Busqueda ")
    base_historial.resizable(0,0)

    frame_borde = Frame(base_historial)
    frame_borde.pack()
    frame_borde.config(width=500, height=500, bg="blue", relief="groove", bd=30)

    #barra de scroll
    barra = Scrollbar(frame_borde, orient=VERTICAL)
    canva_historial = Canvas(frame_borde, bg='white', width=400, height=400, yscrollcommand=barra.set)

    frame_contenido = Frame(canva_historial, bg='white')
    frame_contenido.place(x=0, y=0)

    frame_imagenes = Frame(canva_historial, bg='white')
    frame_imagenes.place(x=200, y=0)
    canva_historial.pack(side="left", fill="both", expand=True)
    canva_historial.create_window(0, 0, window=frame_contenido, anchor="nw")

    barra.config(command=canva_historial.yview)
    barra.pack(side=RIGHT, fill=Y)

    Top_historial = Image.open("Imagenes/Top Historial.png")
    Top_historial = Top_historial.resize((470, 100), Image.ANTIALIAS)
    Top_historial = ImageTk.PhotoImage(Top_historial)
    Top_historial_label = Label(frame_contenido, image=Top_historial)
    Top_historial_label.pack(side = TOP)
    try:
        with open("Programas_Canales/"+usuario+".txt", 'r') as histo:
            invocacion = histo.read()
    except FileNotFoundError:
            invocacion = "Eres nuevo por aqui... No has buscado nada, aun"
    texto = Label(frame_contenido,
                  wraplength=500,
                  text=invocacion,
                  font=('Arial', 10),
                  background="White",
                  anchor="nw",
                  justify=LEFT)
    texto.pack(side = LEFT)
    base_historial.update()
    canva_historial.config(scrollregion=canva_historial.bbox("all"))
    base_historial.config(width=500,height=500,bg="white")
    base_historial.mainloop()

def cierre_de_sesion(menu):
    """
    Según el valor del contador global, determina si los botones de cierre de sesión e historial de búsqueda se
    encuentran ocultos o se enseñan.

    :param menu:
    :return:
    """
    info = messagebox.askyesno(message="¿Esta seguro que desea cerrar sesion?",title = "Aviso")
    if info == True:
        menu.destroy()
        from Login_y_registro import login_grafica
        login_grafica()


def menu_programas(usuario):
    """
    Función donde se ejecuta la interfaz gráfica más grande, donde se encuentran ubicados los botones que invocan ventanas
    emergentes asignadas cada canal correspondiente, además de esto en la parte superior se encuentra la barra de búsqueda
    acompañada del botón de ejecución. Finalmente, en la esquina superior izquierda se muestra la foto de perfil del usuario
    y su nickname.

    :param usuario:
    :return:
    """
    # Caracteristicas de ventana principal
    base = tkinter.Tk()
    base.geometry("1280x720")
    base.title('Buscador de Canales')
    base.config(bg='black')
    base.resizable(0,0)
    # Fondo de la ventana
    fondo = PhotoImage(file="Imagenes\Fondo.png")
    fondo2 = Label(base, image=fondo).place(x=0, y=0)

    # Barra de Busqueda
    barra_busqueda = tkinter.Entry(base, width=90)
    barra_busqueda.place(x=360, y=30)

    #Resultado

    # Boton1 para invocar al canal 1
    fondo_boton1 = Image.open('Imagenes\Logo_CaradeCol.png')
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
    fondo_boton2 = Image.open('Imagenes\Logo_PequeTv.png')
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
    fondo_boton3 = Image.open('Imagenes\Logo_BoomCinema.png')
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

    # Boton4 para invocar al canal 4
    fondo_boton4 = Image.open('Imagenes\Logo_TowerofLaughs.png')
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
    boton4.place(x=120, y=400)

    # Boton5 para invocar al canal 5
    fondo_boton5 = Image.open('Imagenes\Logo_DeepScreams.png')
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
    boton5.place(x=540, y=400)
    # Boton 6 para invocar al canal de proximos estrenos
    fondo_boton6 = Image.open('Imagenes\Proximos estrenos.png')
    fondo_boton6 = fondo_boton6.resize((200, 150), Image.ANTIALIAS)
    fondo_boton6 = ImageTk.PhotoImage(fondo_boton6)
    boton6 = tkinter.Button(base,
                            image=fondo_boton6,
                            text="Proximos Estrenos",
                            compound="top",
                            bg='purple',
                            fg='white',
                            font=("Calibri", 11),
                            command = lambda : ventana_WebScrapping())
    boton6.place(x=960, y=400)

    # Boton7 para busqueda
    fondo_boton7 = Image.open('Imagenes\Lupita.jpg')
    fondo_boton7 = fondo_boton7.resize((15, 15), Image.ANTIALIAS)  # Redimension (Alto, Ancho)
    fondo_boton7 = ImageTk.PhotoImage(fondo_boton7)
    boton7 = tkinter.Button(base, image=fondo_boton7, bg='white', command=lambda: resultado_busqueda(buscador(barra_busqueda.get(),usuario)))
    boton7.place(x=900, y=30)

    #Boton Usuario Y Cierre de Sesion.
    foto_perfil = str(usuario)
    # botones cierre sesion e historial
    cierre_sesion = Button(base,
                           text="Cerrar Sesion",
                           bg="Gray",
                           command = lambda: cierre_de_sesion(base))
    historial =  Button(base,
                        text = "Historial de Busqueda",
                        bg = "gray",
                        command = lambda:ventana_historial(usuario))
    def mostrar_ocultar():
        global contador
        if contador == 0:
            cierre_sesion.place_forget()
            historial.place_forget()
            contador += 1
        else:
            cierre_sesion.place(x=85, y=10)
            historial.place(x = 85, y = 50)
            contador = 0
    try:

        imagen_profile = Image.open("Imagenes/" + foto_perfil + ".png")
        imagen_profile = imagen_profile.resize((50, 50), Image.ANTIALIAS)  # Redimension (Alto, Ancho)
        imagen_profile = ImageTk.PhotoImage(imagen_profile)
        boton_usuario = Button(base,
                               image=imagen_profile,
                               text=str(usuario),
                               compound="top",
                               bg='Black',
                               fg='white',
                               font=("Calibri", 11),
                               command = lambda :mostrar_ocultar())
        boton_usuario.place(x=5, y=5)

        base.mainloop()
    except FileNotFoundError:
        imagen_profile = Image.open("Imagenes/default.png")
        imagen_profile = imagen_profile.resize((50, 50), Image.ANTIALIAS)  # Redimension (Alto, Ancho)
        imagen_profile = ImageTk.PhotoImage(imagen_profile)
        boton_usuario = Button(base,
                               image=imagen_profile,
                               text=str(usuario),
                               compound="top",
                               bg='Black',
                               fg='white',
                               font=("Calibri", 10),
                               command = lambda :mostrar_ocultar())
        boton_usuario.place(x=5, y=5)
        base.mainloop()