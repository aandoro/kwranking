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

def opcion_seleccionada(opcion):
    if opcion == 1:
        return carga_keywords()
    elif opcion == 2:
        muestra_keywords()
        return ''
    elif opcion == 3:
        print('')
        kw = input('Ingrese la palabra a buscar:')
        dominio = input('Ingrese en que dominio tiene que buscarlo:')
        posicion = comprueba_keywords(kw, dominio)
        if posicion < 100:
            return f'Las keywords {kw} se han encontrado en la posición {posicion} para el dominio {dominio}'
        else:
            return f'De momento, las keywords {kw} no rankean para el dominio {dominio}'
    else:
        return 'Opción no válida'