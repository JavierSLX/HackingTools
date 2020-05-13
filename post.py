#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
import argparse
from os import path

#Crea los argumentos que aceptará el script
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help="Indica el archivo a subir")
parser = parser.parse_args()

def main():
    if parser.file:
        #Verifica que existe el archivo y lo sube a una url
        if path.exists(parser.file):
            archivo = open(parser.file, "rb")
            headers = {"User-Agent": "Firefox"}
            response = requests.post(url="https://curso--python-0-prueba-pentest1.000webhostapp.com", files={"uploaded_file": archivo}, headers=headers)

            #Checa si el archivo se encuentra en la respuesta para confirmar que se subio
            ruta = parser.file.split("\\")
            if ruta[len(ruta) - 1] in response.text:
                print("Archivo subido con exito")
            else:
                print("Falló la subida del archivo")
        else:
            print("No existe el archivo")
    else:
        print("Necesita agregar un archivo para subir")

if __name__ == '__main__':
    main()