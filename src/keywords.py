import requests
from bs4 import BeautifulSoup
from src.model import Keyword

url = 'https://www.google.com/search?'

def carga_keywords():
    keywords = []
    posicion = 1
    try:
        with open('keywords.txt') as fichero:
            for kw in fichero:
                kw = kw.replace('\n', '')
                kw_db = Keyword(kw,posicion)
                posicion += 1
                kw_db.save()
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

def comprueba_keywords(kw, dominio):
    continuar = True
    posicion = 1
    encontrado = False
    parametros = {'q':kw,'start':0}
    while continuar and not encontrado:
        resp = requests.get(url,params=parametros)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'lxml')
            div_main = soup.find(id='main')
            resultados = div_main.find_all('div', {'class', 'ZINbbc xpd O9g5cc uUPGi'})
            for res in resultados:
                if res.div and res.div.a:
                    if aparece_el_dominio(res.div.a['href'], dominio):
                        encontrado = True
                        break
                    else:
                        posicion += 1
            if not encontrado:
                footer = div_main.find('footer')
                siguiente = footer.find('a', {'aria-label': 'Página siguiente'})
                if siguiente:
                    parametros['start'] += 10
                    if parametros['start'] == 100:
                        continuar = False
                else:
                    continuar = False
        else:
            continuar = False
    if not encontrado:
        posicion = 100
    return posicion

def aparece_el_dominio(link, dominio):
    encontrado = False
    fin = link.find('&')
    pagina = link[:fin]
    if dominio in pagina:
        encontrado = True
    return encontrado