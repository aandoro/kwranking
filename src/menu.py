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
        comprueba_keywords()
    else:
        return 'Opción no válida'