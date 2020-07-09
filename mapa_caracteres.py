
def mapa_caracteres(cadena):
    contador = 0
    resultado = []
    for elem in cadena:
        try:
            index = cadena.index(elem)
            index_res = resultado.index(index)
            resultado.append(index_res)
        except ValueError:
            resultado.append(contador)
            contador+=1
    return resultado

cadena = input('Ingrese una palabra: ')

list = mapa_caracteres(cadena)

print(list)