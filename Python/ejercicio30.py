'''Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.'''


def elementos_unicos(lista):
    # Usamos un conjunto para eliminar duplicados
    conjunto_unicos = set(lista)
    # Convertimos el conjunto de nuevo a una lista
    lista_unicos = list(conjunto_unicos)
    return lista_unicos


mi_lista = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = elementos_unicos(mi_lista)

print(f'Lista original: {mi_lista}')
print(f'Lista sin duplicados: {lista_sin_duplicados}')
