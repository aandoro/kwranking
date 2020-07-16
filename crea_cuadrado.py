
def cuadrado(n):
    if n == 0:
        return []
    else:
        return [[n for _ in range(n)] for _ in range(n)]

numero = -1
while numero < 0:
    numero = int(input('ingrese un numero mayor o igual a 0: '))

print(cuadrado(numero))