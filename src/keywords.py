import requests
import lxml

def carga_keywords():
    keywords = []
    try:
        with open('keywords.txt') as fichero:
            for kw in fichero:
                kw = kw.replace('\n', '')
                keywords.append(kw)
    except FileNotFoundError:
        print('No se encuentra el fichero keywords.txt')
    return keywords

def muestra_keywords():
    print('')
    keywords = carga_keywords()
    contador = 0
    for kw in keywords:
        print(kw)
        contador += 1
        if contador == 20:
            contador = 0
            input('Mostrar más...')

def comprueba_keywords(kw,domino):
    print('nuevo metodo')