'''Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.'''


def tienen_elemento_en_comun(lista1, lista2):
    for elemento in lista1:
        if elemento in lista2:
            return True
    return False


lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 6, 7, 8, 9]
resultado = tienen_elemento_en_comun(lista1, lista2)

if resultado:
    print('Las listas tienen al menos un elemento en común.')
else:
    print('Las listas no tienen elementos en común.')
