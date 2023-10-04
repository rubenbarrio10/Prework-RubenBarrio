'''Define una función que tome una lista y retorne la lista sin duplicados.'''


def eliminar_duplicados(lista):
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados


mi_lista = [1, 2, 2, 3, 4, 4, 5]
sin_duplicados = eliminar_duplicados(mi_lista)

print(f'Lista original: {mi_lista}')
print(f'Lista sin duplicados: {sin_duplicados}')
