import ast

entrada = input("Ingreso de ciudades {'ciudad:poblacion',}: ")

def ordena_ciudades(ciudades):
    print(', '.join([f'{k}' for k, v in ciudades.items() if v > 200000]))

ordena_ciudades(ast.literal_eval(entrada))