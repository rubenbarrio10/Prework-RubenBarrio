'''Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).'''


def interseccion_listas(lista1, lista2):
    # Convertimos ambas listas en conjuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    # Calculamos la intersección de los conjuntos
    interseccion = conjunto1.intersection(conjunto2)
    # Convertimos la intersección de nuevo en una lista
    resultado = list(interseccion)
    return resultado


lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

resultado_interseccion = interseccion_listas(lista1, lista2)
print(f'Intersección de las listas: {resultado_interseccion}')
