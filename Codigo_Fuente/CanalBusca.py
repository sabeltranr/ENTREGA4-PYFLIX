import Historial
from Historial import historial_busqueda
def canal_accion():
    """
        Obtener la programacion del canal de accion, almacenada en un archivo.txt.
        :return: Contenido de la programacion en forma de lista,
        donde cada elemento es un programa con su hora,nombre y sinopsis.
    """
    archivo_accion = open("Programas_Canales\canal_accion.txt")
    texto_accion = archivo_accion.read()
    archivo_accion.close()
    lineas_accion = texto_accion.split("\n")
    return lineas_accion
def canal_infantil():
    """
        Obtener la programacion del canal de infantil, almacenada en un archivo.txt.
        :return: Contenido de la programacion en forma de lista,
        donde cada elemento es un programa con su hora,nombre y sinopsis.
        """
    archivo_infantil = open("Programas_Canales\canal_infantil.txt")
    texto_infantil = archivo_infantil.read()
    archivo_infantil.close()
    lineas_infantil = texto_infantil.split("\n")
    return lineas_infantil

def canal_terror():
    """
        Obtener la programacion del canal de terror, almacenada en un archivo.txt.
        :return: Contenido de la programacion en forma de lista,
        donde cada elemento es un programa con su hora,nombre y sinopsis.
        """
    archivo_terror = open("Programas_Canales\canal_terror.txt")
    texto_terror = archivo_terror.read()
    archivo_terror.close()
    lineas_terror = texto_terror.split("\n")
    return lineas_terror

def canal_comedia():
    """
        Obtener la programacion de canal de Comedia, almacenada en un archivo.txt.
        :return: Contenido de la programacion en forma de lista,
        donde cada elemento es un programa con su hora,nombre y sinopsis.
    """
    archivo_comedia = open("Programas_Canales\canal_comedia.txt")
    texto_comedia = archivo_comedia.read()
    archivo_comedia.close()
    lineas_comedia = texto_comedia.split("\n")
    return lineas_comedia
def canal_peliculas():
    """
        Obtener la programacion de canal de accion, almacenada en un archivo.txt.
        :return: Contenido de la programacion en forma de lista,
        donde cada elemento es un programa con su hora,nombre y sinopsis.
    """
    archivo_peliculas = open("Programas_Canales\canal_peli.txt")
    texto_peliculas = archivo_peliculas.read()
    archivo_peliculas.close()
    lineas_peliculas = texto_peliculas.split("\n")
    return lineas_peliculas
def mashup():
    """
        Obtener la programacion en forma de lista de los canales de acción, comedia, terror, infantil, y de peliculas
        para unirlas en una sola lista
        :return: Una lista donde cada elemento contenido es una sublista, que representa la programación de un canal
        """
    lista_canales = [canal_infantil(),canal_accion(),canal_terror(),canal_comedia(),canal_peliculas()]
    return lista_canales
def buscador(entrada_barrabusqueda,usuario):
    """
    Toma los datos que ingresa el usuario y busca el programa solicitado dentro del contenido de todos los canales, además
    del nombre del usuario, para realizar el registro en su historial de búsqueda.

    :param entrada_barrabusqueda:
    :param usuario:
    :return Si se encuentra el programa solicitado a partir de las palabras ingresadas, regresa el nombre del canal
    donde se emite, el horario de presentación, nombre del programa relacionado con la búsqueda y sinopsis del mismo, de
    lo contario se mostrar que no existe elementos relacionados con lo solicitado.
    Dicha informacion se muestra en una ventana emergente en la ventana principal:
    """
    historial_busqueda(entrada_barrabusqueda,usuario)
    resultado_final = ""
    lineas = mashup()
    contador = 0
    nombre_canales=["PequeTv", "Boom Cinema", "Deep Scream", "Tower Of Laughs","Cara De Col"]
    imagen = ''
    #Acceder a cada elemento del mashup (canal)
    for macro_elemento in range(len(lineas)):
    #Acceder a cada sublista, dicho elemento contiene la programacion de todo un canal
        for elemento in range(len(lineas[macro_elemento])):
    #Separar el canal por hora, nombre y sinopsis de cada programa
            lista_elemento = lineas[macro_elemento][elemento].split("|")
    #Buscar dentro de cada sublista el elemento solicitado
            for dentro_elemento in lista_elemento:
                if entrada_barrabusqueda in dentro_elemento:
                    contador += 1
                    resultado_encontrad = "Canal: "+nombre_canales[macro_elemento]+'\n'+ "Hora: "+ lista_elemento[0]+\
                                        '\n'+"Programa :"+lista_elemento[1] +'\n\n'+ "Sinopsis: "+ lista_elemento[2]
                    resultado_final += resultado_encontrad + '\n'
                    resultado_final += '\n\n'
    if contador == 0:
        error =  ("El criterio de busqueda "+'"'+entrada_barrabusqueda+'"'+" no fue encontrado dentro de ninguna programación")
        return error
    else:
        return resultado_final


