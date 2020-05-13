#!/usr/bin/env python
#_*_ coding: utf8 _*_

from Wappalyzer import WebPage, Wappalyzer
import argparse

#Crea los argumentos que aceptará el script
parser = argparse.ArgumentParser(description="Detector de tecnologias")
parser.add_argument("-t", "--target", help="Objetivo a analizar")
parser = parser.parse_args()

def main():
    if parser.target:
        wap = Wappalyzer.latest()
        try:
            web = WebPage.new_from_url(parser.target)
            tecnologias = wap.analyze(web)
            for tecnologia in tecnologias:
                print("Tecnología detectada: {}".format(tecnologia))
        except:
            print("Ha ocurrido un error")
    else:
        print("Imposible analizar el objetivo")

if __name__ == "__main__":
    main()