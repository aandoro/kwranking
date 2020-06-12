from src.keywords import carga_keywords, muestra_keywords, comprueba_keywords, keywords_como_lista_de_valores
from src.datos import exportar_resultados_a_xlsx
from src.model import Keyword

def muestra_menu():
    print('')
    print('')
    print('-------- Kwranking --------')
    print('')
    print('[1] – Importar palabras clave')
    print('[2] – Mostrar palabras clave')
    print('[3] – Comprobar palabras clave')
    print('[4] – Exportar a xlsx')
    print('[0] – Salir')

def opcion_seleccionada(opcion, kws):
    if opcion == 1:
        carga_keywords()
        return Keyword.get_all()
    elif opcion == 2:
        muestra_keywords(kws)
    elif opcion == 3:
        print('')
        dominio = input('Ingrese en que dominio tiene que buscarlo: ')
        for kw in kws:
            posicion = comprueba_keywords(kw.keyword, dominio)
            if posicion < 100:
                kw_db = kw.update(posicion)
                kw_db.posicion = posicion
                kw_db.save()
    elif opcion == 4:
        keywords_tuplas = keywords_como_lista_de_valores(kws)
        exportar_resultados_a_xlsx(keywords_tuplas)
    else:
        return 'Opción no válida'