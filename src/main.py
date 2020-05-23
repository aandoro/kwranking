from src.menu import muestra_menu, opcion_seleccionada

def run():
    keywords = []
    while True:
        muestra_menu()
        opcion = input('Selecciona una opción > ')
        try:
            if int(opcion) == 0:
                break
            else:
                keywords = opcion_seleccionada(int(opcion))
                print('')
                print(keywords)
        except ValueError:
            print('')
            print('La opcion no era numerica')
        
    