#!/usr/bin/env python
#_*_ coding: utf8 _*_

import mechanize
import argparse
from bs4 import BeautifulSoup

#Crea los argumentos que aceptará el script
parser = argparse.ArgumentParser()
parser.add_argument("-b", "--buscar", help="Opcion a buscar")
parser = parser.parse_args()

def main():
    if parser.buscar:
        #Crea una instancia del navegador y lo configura para su uso
        navegador = mechanize.Browser()
        navegador.set_handle_robots(False)
        navegador.set_handle_equiv(False)
        navegador.addheaders = [('User-Agent', "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.0")]

        #Abre el navegador, el link y realiza la busqueda
        navegador.open("https://www.google.com")

        #Posicion del textbox, agrega lo que se va a buscar y presiona enter
        navegador.select_form(nr=0)
        navegador["q"] = parser.buscar
        navegador.submit()
        html = BeautifulSoup(navegador.response().read(), "html5lib")

        #Obtenemos las etiquetas "a" donde se encuentran los resultados de la búsqueda
        for link in html.find_all("a"):
            contenido = link.get("href")
            contenido = contenido.replace("/url?q=", "")
            print(contenido)
    else:
        print("Palabra a buscar")

if __name__ == "__main__":
    main()