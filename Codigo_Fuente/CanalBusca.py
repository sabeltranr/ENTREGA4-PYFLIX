def canal_accion():
    """
        Obtener la programacion del canal de accion, almacenada en un archivo.txt.
        :return: Contenido de la programacion en forma de lista,
        donde cada elemento es un programa con su hora,nombre y sinopsis.
    """
    archivo_accion = open("canal_accion.txt")
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
    archivo_infantil = open("canal_infantil.txt")
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
    archivo_terror = open("canal_terror.txt")
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
    archivo_comedia = open("canal_comedia.txt")
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
    archivo_peliculas = open("canal_peli.txt")
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
def buscador(entrada_barrabusqueda):
    """
    Toma los datos que ingresa el usuario y busca el programa solicitado dentro del contenido de todos los canales
    :param entrada_barrabusqueda:
    :return: Si se encuentra el programa solicitado a partir de las palabras ingresadas, regresa el nombre del canal donde se emite,
    el horario de presentación, nombre del programa relacionado con la busqueda y sinopsis del mismo.
    Dicha informacion se imprime en la consola (por el momento).
    """
    lineas = mashup()
    nombre_canales=["PequeTv", "Boom Cinema", "Deep Scream", "Tower Of Laughs","Cara De Col"]
    #Acceder a cada elemento del mashup (canal)
    for macro_elemento in range(len(lineas)):
    #Acceder a cada sublista, dicho elemento contiene la programacion de todo un canal
        for elemento in range(len(lineas[macro_elemento])):
    #Separar el canal por hora, nombre y sinopsis de cada programa
            lista_elemento = lineas[macro_elemento][elemento].split("|")
    #Buscar dentro de cada sublista el elemento solicitado
            for dentro_elemento in lista_elemento:
                if entrada_barrabusqueda in dentro_elemento:
                    # print(lista_elemento)
                    print("Canal: ",nombre_canales[macro_elemento])
                    print("Hora: ", lista_elemento[0])
                    print("Programa: ", lista_elemento[1])
                    print("Sinopsis: ", lista_elemento[2])
                    print("------------------------------------------------")


