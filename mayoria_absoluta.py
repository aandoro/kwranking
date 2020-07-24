
def mayoria_absoluta(votos):
    mitad_elementos = len(votos) / 2
    if votos:
        resultado = [(votos[voto], votos.count(votos[voto])) for voto in range(len(votos)) if votos[voto] != votos[voto-1]]
        for voto, cantidad in resultado:
            if cantidad > mitad_elementos:
                return voto

print(f'Lista vacia: {mayoria_absoluta([])}')

print(f"Mayor que la mitad: {mayoria_absoluta(['A', 'A', 'B'])}")

print(f"Mayor que la mitad: {mayoria_absoluta(['A', 'A', 'A', 'B', 'C', 'A'])}")

print(f"No hay elementos mayoritarios: {mayoria_absoluta([['A', 'B', 'B', 'A', 'C', 'C']])}")
