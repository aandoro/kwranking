from src.keywords import carga_keywords, muestra_keywords, comprueba_keywords

def muestra_menu():
    print('')
    print('')
    print('-------- Kwranking --------')
    print('')
    print('[1] – Importar palabras clave')
    print('[2] – Mostrar palabras clave')
    print('[3] - Comprobar palabras clave')
    print('[0] – Salir')

def opcion_seleccionada(opcion, kws):
    if opcion == 1:
        return carga_keywords()
    elif opcion == 2:
        muestra_keywords()
        return ''
    elif opcion == 3:
        print('')
        #kw = input('Ingrese la palabra a buscar:')
        dominio = input('Ingrese en que dominio tiene que buscarlo:')
        for kw in kws:
            posicion = comprueba_keywords(kw.keyword, dominio)
            if posicion < 100:
                kw.posicion = posicion
                kw.update()
        return kws
    else:
        return 'Opción no válida'