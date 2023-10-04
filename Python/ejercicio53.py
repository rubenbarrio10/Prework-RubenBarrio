'''Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.'''


def elementos_no_comunes(lista1, lista2):
    elementos_no_comunes = [elemento for elemento in lista1 if elemento not in lista2] + [
        elemento for elemento in lista2 if elemento not in lista1]
    return elementos_no_comunes


lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
resultado = elementos_no_comunes(lista1, lista2)

print(f'Elementos no comunes entre las listas: {resultado}')
