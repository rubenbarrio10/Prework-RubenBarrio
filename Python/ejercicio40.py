'''Define una función que tome una lista y retorne la lista ordenada en orden ascendente.'''


def ordenar_ascendente(lista):
    # Usamos la función sorted para obtener una nueva lista ordenada
    lista_ord = sorted(lista)
    return lista_ord


mi_lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
lista_ordenada = ordenar_ascendente(mi_lista)

print(f'Lista original: {mi_lista}')
print(f'Lista ordenada en orden ascendente: {lista_ordenada}')
