#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
import argparse

#Crea los argumentos que aceptará el script
parser = argparse.ArgumentParser(description="Detector de cabeceras")
parser.add_argument("-t", "--target", help="Objetivo")
parser = parser.parse_args()


def main():
    #Valida que exista un objetivo
    if parser.target:
        try:
            #Trata de conectarse a la url que se le pasó
            response = requests.get(url=parser.target)

            #Imprime las cabeceras
            cabeceras = dict(response.headers)
            for key in cabeceras:
                print("{} : {}".format(key, cabeceras[key]))
        except:
            print("No me pude conectar a {}".format(parser.target))
    else:
        print("No hay objetivo")

if __name__ == '__main__':
    main()