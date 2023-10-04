'''Define una función que encuentre el elemento más común en una lista.'''

from collections import Counter


def elemento_mas_comun(lista):
    # Usamos Counter para contar las ocurrencias de cada elemento en la lista
    conteo = Counter(lista)
    # Encontramos el elemento con el recuento más alto
    elemento_comun = conteo.most_common(1)[0][0]
    return elemento_comun


mi_lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
elemento_comun = elemento_mas_comun(mi_lista)

print(f'El elemento más común en la lista es: {elemento_comun}')
