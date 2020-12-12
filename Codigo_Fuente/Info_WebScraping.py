from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen

def web_scraping(titulo,fecha):

    """
        Obtener el nombre de la pelicula que se estrena y la fecha de
        la pagina web,lo guarda en un archivo .txt
        :param class 'bs4.element.ResultSet' titulo: lista filtrada de los nombres de
        cada uno de los estrenos
        :param class 'list' fecha: lista filtrada de los dias de
        cada uno de los estrenos
    """

    fecha_estreno = list(map(str, fecha))
    titulo_estreno = list(map(str, titulo))
    web = "web"

    try:
        archivo_titulofecha = open("web.txt", "r")
        archivo_titulofecha.close()

    except:
        with open('web.txt', "a+") as   web:
            for j in range(len(fecha_estreno)):
                web.write(titulo_estreno[j][5:-6]+"  -  "+fecha_estreno[j][8:-9]+"\n")

def imagen(image):

    """
        Obtener y descargar de la pagina web las imagenes
        de algunas peliculas,y las guarda con el nombre de
        la pelicula.
        :param class 'bs4.element.ResultSet' image : resultado
        del filtrado el cual contiene el nombre de la pelicula y el
        url de la imagen de cada pelicula.
    """

    dic = {}
    f = image[0].get('src') #url de la imagen
    n = image[0].get('alt') #nombre del estreno
    dic[n] = f

    for elemento in dic:
        nombre=str(elemento)+".png"
        urllib.request.urlretrieve(dic[elemento], nombre)

def obtencion_De_datos():

    """
        Recibe el url de la pagina web, la traduce y filtra por
        etiquetas, llama a las funciones que realizan la otencion de
        titulo y fecha del estreno junto a la funcion que obtiene
        las imagenes de estos estrenos.
    """

    url = "file:///C:/Users/luisv/PycharmProjects/pythonProject4/Programas_canales/webscraping.html"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    titulos = (soup.find_all("h2"))
    fechas = (soup.find_all("strong"))
    fechas = fechas[1:]
    imagen_inicio = soup.find_all("img")
    imagen(imagen_inicio)
    web_scraping(titulos, fechas)
