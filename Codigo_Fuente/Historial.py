import datetime
def historial_busqueda(resultado, usuario):
    """
    Recibe como parámetro el usuario en sesión y el comando de búsqueda ingresado en la barra de búsqueda, esto para
    almacenarlo en un archivo.txt que funciona como registro de los elementos buscados y la hora de dicha búsqueda.
    Si no existe registro previo o el usuario es nuevo, se crea un nuevo archivo donde se guarda su historial.

    :param resultado:
    :param usuario:
    :return:
    """
    dt = datetime.datetime.now()
    fecha_hora = str(dt)[:-7]
    with open("Programas_Canales/" + usuario + '.txt', "a+") as historial:
        historial.write("Criterio de busqueda: "+resultado + "\n"+"Fecha y horario de busqueda: " + fecha_hora + '\n\n')