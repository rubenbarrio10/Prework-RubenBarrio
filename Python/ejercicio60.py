'''Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.'''


def ordenar_por_ultimo_elemento(tuplas):
    # Utilizamos una función lambda como clave de ordenamiento para sorted.
    # La función lambda toma una tupla y retorna su último elemento.
    return sorted(tuplas, key=lambda x: x[-1])


lista_de_tuplas = [(1, 3, 5), (2, 4, 1), (5, 1, 2)]
lista_ordenada = ordenar_por_ultimo_elemento(lista_de_tuplas)

print(f'Lista original de tuplas: {lista_de_tuplas}')
print(f'Lista ordenada por el último elemento de cada tupla: {lista_ordenada}')
