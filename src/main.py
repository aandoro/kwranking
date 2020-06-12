from src.menu import muestra_menu, opcion_seleccionada
from src.model import Keyword

def run():
    keywords = Keyword.get_all()
    while True:
        muestra_menu()
        opcion = int(input('Selecciona una opción > '))
        try:
            if int(opcion) == 0:
                break
            else:
                opcion_seleccionada(opcion, keywords)
        except ValueError:
            print('')
            print('La opcion no era numerica')
        
    